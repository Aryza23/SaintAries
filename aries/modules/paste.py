import asyncio
import os
import re

import aiofiles
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message
from asyncio import get_running_loop

from aries import pbot as app
from aries import pbot, aiohttpsession, eor
from aries.utils.errors import capture_err
from aries.utils.pastebin import epaste, hpaste
from aries.utils.keyboard import ikb

__mod_name__ = "Paste"

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with aiohttpsession.head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return status == 200
    return False


@pbot.on_message(filters.command("hpaste") & ~filters.edited)
@capture_err
async def paste_func(_, message: Message):
    if not message.reply_to_message:
        return await eor(message, text="Reply To A Message With /paste")
    r = message.reply_to_message

    if not r.text and not r.document:
        return await eor(message, text="Only text and documents are supported.")

    m = await eor(message, text="Pasting...")

    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("You can only paste files smaller than 40KB.")

        if not pattern.search(r.document.mime_type):
            return await m.edit("Only text files can be pasted.")

        doc = await message.reply_to_message.download()

        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()

        os.remove(doc)

    link = await hpaste(content)
    kb = ikb({"Paste Link": link})
    try:
        if m.from_user.is_bot:
            await message.reply_photo(
                photo=link,
                quote=False,
                reply_markup=kb,
            )
        else:
            await message.reply_photo(
                photo=link,
                quote=False,
                caption=f"**Paste Link:** [Here]({link})",
            )
        await m.delete()
    except Exception:
        await m.edit("Here's your paste", reply_markup=kb)


@app.on_message(filters.command("paste") & ~filters.edited)
@capture_err
async def epaste_func(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply To A Message With /paste")
    m = await message.reply_text("Pasting...")
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("You can only paste files smaller than 1MB.")
        if not pattern.search(document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await epaste(content)
    preview = link + "/preview.png"
    button = InlineKeyboard(row_width=1)
    button.add(InlineKeyboardButton(text="Paste Link", url=link))

    if await isPreviewUp(preview):
        try:
            await message.reply_photo(photo=preview, quote=False, reply_markup=button)
            return await m.delete()
        except Exception:
            pass
    return await m.edit(link)
