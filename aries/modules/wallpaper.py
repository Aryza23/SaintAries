# Copyright 2021 ©
# Modul Create by https://t.me/xflicks | Github = https://github.com/FeriEXP
# Yang remove cacat

import os
from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError

from aries import telethn as tbot
from aries.events import register
from aries import ubot


@register(pattern="^/wall ?(.*)")
async def _(event):
    try:
        query = event.pattern_match.group(1)
        feri = await event.reply("`Searching for Images What you're looking for.....`")
        async with ubot.conversation("@AnosVoldigoadbot") as conv:
            try:
                query1 = await conv.send_message(f"/wall {query}")
                r1 = await conv.get_response()
                r2 = await conv.get_response()
                await ubot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await feri.edit("`Emrorr lol`")
            if r1.text.startswith("No"):
                return await feri.edit(f"`Cannot find the image`")
            img = await ubot.download_media(r1)
            img2 = await ubot.download_media(r2)
            await feri.edit("`Sending Image....`")
            p = await tbot.send_file(
                event.chat_id,
                img,
                force_document=False,
                reply_to=event.reply_to_msg_id,
            )
            await tbot.send_file(
                event.chat_id,
                img2,
                force_document=True,
                reply_to=p,
            )
            await feri.delete()
            await ubot.delete_messages(conv.chat_id, [r1.id, r2.id, query1.id])
        await event.delete()
        os.system("rm *.png *.jpg")
    except TimeoutError:
        return await feri.edit("`Cannot find the image`")
