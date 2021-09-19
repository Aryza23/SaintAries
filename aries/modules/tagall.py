# @ImJanindu <https://t.me/Infinity_BOTs>
# Mizuki Tagall

import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from Mizuk# @ImJanindu <https://t.me/Infinity_BOTs>
# Mizuki Tagall

import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
from aries import tbot as bot
import telethon
from telethon import events


@bot.on(events.NewMessage(pattern="/tagall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return # @ImJanindu
    mentions = event.pattern_match.group(1)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@bot.on(events.NewMessage(pattern="/administrator"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Admins in this chat:** "
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__help__ = """
I can tag all members in group with a message.
• `/tagall <message>`*:* tag all members in the group with given message.
*NOTE:* Tagger only works on groups which have less than 100 members.
"""

__mod_name__ = "Tagger"i import tbot as bot
import telethon
from telethon import events


@bot.on(events.NewMessage(pattern="/tagall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return # @ImJanindu
    mentions = event.pattern_match.group(1)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@bot.on(events.NewMessage(pattern="/administrator"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Admins in this chat:** "
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__help__ = """
I can tag all members in group with a message.
• `/tagall <message>`*:* tag all members in the group with given message.
*NOTE:* Tagger only works on groups which have less than 100 members.
"""

__mod_name__ = "Tagger"
