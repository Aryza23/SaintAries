from aries import CMD_HELP, BOT_ID
import os
from aries import tbot
from time import time

import aries.modules.sql.chatbot_sql as sql
from coffeehouse.api import API
from coffeehouse.exception import CoffeeHouseError as CFError
from coffeehouse.lydia import LydiaAI
from aries import LYDIA_API_KEY, OWNER_ID
from telethon import types
from telethon.tl import functions
from aries.event import register
from telethon import events

CoffeeHouseAPI = API(LYDIA_API_KEY)
api_client = LydiaAI(CoffeeHouseAPI)


async def can_change_info(message):
    try:
        result = await tbot(
            functions.channels.GetParticipantRequest(
                channel=message.chat_id,
                user_id=message.sender_id,
            )
        )
        p = result.participant
        return isinstance(p, types.ChannelParticipantCreator) or (isinstance(
            p, types.ChannelParticipantAdmin) and p.admin_rights.change_info)
    except Exception:
        return False


@register(pattern="^/addchat$")
async def _(event):
    if event.is_group:
        if not await can_change_info(message=event):
            return
    else:
        return

    global api_client
    chat = event.chat
    send = await event.get_sender()
    user = await tbot.get_entity(send)
    is_chat = sql.is_chat(chat.id)
    if not is_chat:
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        sql.set_ses(chat.id, ses_id, expires)
        await event.reply("AI successfully enabled for this chat!")
        return
    await event.reply("AI is already enabled for this chat!")
    return ""


@register(pattern="^/rmchat$")
async def _(event):
    if event.is_group:
        if not await can_change_info(message=event):
            return
    else:
        return
    chat = event.chat
    send = await event.get_sender()
    user = await tbot.get_entity(send)
    is_chat = sql.is_chat(chat.id)
    if not is_chat:
        await event.reply("AI isn't enabled here in the first place!")
        return ""
    sql.rem_chat(chat.id)
    await event.reply("AI disabled successfully!")


@tbot.on(events.NewMessage(pattern=None))
async def check_message(event):
    if event.is_group:
        pass
    else:
        return
    message = str(event.text)
    reply_msg = await event.get_reply_message()
    if message.lower() == "julia":
        return True
    if reply_msg:
        if reply_msg.sender_id == BOT_ID:
            return True
    else:
        return False


@tbot.on(events.NewMessage(pattern=None))
async def _(event):
    if event.is_group:
        pass
    else:
        return
    global api_client
    msg = str(event.text)
    chat = event.chat
    is_chat = sql.is_chat(chat.id)
    if not is_chat:
        return
    if msg:
        if not await check_message(event):
            return
        sesh, exp = sql.get_ses(chat.id)
        query = msg
        try:
            if int(exp) < time():
                ses = api_client.create_session()
                ses_id = str(ses.id)
                expires = str(ses.expires)
                sql.set_ses(chat.id, ses_id, expires)
                sesh, exp = sql.get_ses(chat.id)
        except ValueError:
            pass
        try:
            async with tbot.action(event.chat_id, 'typing'):
                rep = api_client.think_thought(sesh, query)
                await event.reply(rep)
        except CFError as e:
            print(e)

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /addchat: Activates AI mode in the chat the bot will give auto replies to anyone who tags the bot
 - /rmchat: Deactivates AI mode in the chat the bot will stop giving auto replies to anyone who tags the bot
"""

CMD_HELP.update({
    file_helpo: [
        file_helpo,
        __help__
    ]
})
