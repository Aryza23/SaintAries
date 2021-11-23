import os
from telethon.errors.rpcerrorlist import YouBlockedUserError

from aries.events import register
from aries import ubot
from aries import TEMP_DOWNLOAD_DIRECTORY
from aries import telethn as tbot


@register(outgoing=True, pattern=r"^/kamuii(:? |$)([1-8])?")
async def _(event):
    aryza = await event.reply(
        "`Prosess, Berubah menjadi srirahanjing, jurus di aktifkan...`"
    )
    level = event.pattern_match.group(2)
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await aryza.edit("`Mohon Balas Di Sticker`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await aryza.edit("`Gambar tidak di dukung`")
        return
    if reply_message.sender.ubot:
        await aryza.edit("`Mohon Balas Di Sticker`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = event.message.reply_to_msg_id
    async with ubot.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await ubot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await aryza.edit("`Mohon Unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Forward"):
            await aryza.edit("`Mohon Matikan Setelan Forward Privasi...`")
        else:
            downloaded_file_name = await ubot.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await ubot.delete_messages(conv.chat_id, [msg.id, response.id])
            else:
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, response.id, r.id, msg_level.id]
                )
    await aryza.delete()
    await event.delete()
    return os.remove(downloaded_file_name)


@register(outgoing=True, pattern=r"^/df(:? |$)([1-8])?")
async def _(event):
    aryza = await event.reply("`Sedang Dalam Proses......`")
    level = event.pattern_match.group(2)
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await aryza.edit("`Mohon Balas Di Sticker`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await aryza.edit("`Mohon Balas Di Sticker`")
        return
    if reply_message.sender.ubot:
        await aryza.edit("`Mohon Balas Di Sticker`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = event.message.reply_to_msg_id
    async with ubot.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await ubot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await aryza.edit("`Mohon Unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Forward"):
            await aryza.edit("`Mohon Matikan Setelan Privasi Forward...`")
        else:
            downloaded_file_name = await ubot.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await ubot.delete_messages(conv.chat_id, [msg.id, response.id])
            else:
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, response.id, r.id, msg_level.id]
                )
    await aryza.delete()
    await event.delete()
    return os.remove(downloaded_file_name)


"""
CMD_HELP.update({
    "kamuii":
    "`.kamuii` or `.kamuii` [level(1-8)]"
    "\nUsage: untuk mengubah foto/sticker."
})
"""
