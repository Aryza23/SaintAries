# @ImJanindu <https://t.me/Infinity_BOTs>
# Mizuki Tagall

import asyncio

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from aries import telethn as bot


@bot.on(events.NewMessage(pattern="^/tagall|/mall|/tall|/all|#all|@all ?(.*)"))
async def mentionall(event):
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    admins = []
    async for admin in bot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        admins.append(admin.id)
    if not event.sender_id in admins:
        return await event.respond("🔴 YOU ARE NOT AN ADMIN IN THESE GROUP")

    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.reply_to_msg_id:
        mode = "text_on_reply"
        msg = event.reply_to_msg_id
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which sended before i added to group)__"
            )
    elif event.pattern_match.group(1) and event.reply_to_msg_id:
        return await event.respond("__Give me one argument!__")
    else:
        return await event.respond(
            "GIVE ME A TEXT TO TAG MEMBERS OR REPLY TO A TEXT WHICH YOU WANTS TO TAG ALL"
        )

    if mode == "text_on_cmd":
        usrnum = 0
        usrtxt = ""
        async for usr in bot.iter_participants(event.chat_id):
            usrnum += 1
            usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
            if usrnum == 5:
                await bot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
                await asyncio.sleep(2)
                usrnum = 0
                usrtxt = ""

    if mode == "text_on_reply":
        usrnum = 0
        usrtxt = ""
        async for usr in bot.iter_participants(event.chat_id):
            usrnum += 1
            usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
            if usrnum == 5:
                await bot.send_message(event.chat_id, usrtxt, reply_to=msg)
                await asyncio.sleep(2)
                usrnum = 0
                usrtxt = ""


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
❍ `/tagall <message>`*:* tag all members in the group with given message.
🔘 *NOTE:* Tagger only works on groups which have less than 100 members.
"""

__mod_name__ = "🔘 Mention"
