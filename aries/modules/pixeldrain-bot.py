# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Pixeldrain-Bot/blob/main/LICENSE

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aries.more import pixeldrain
from aries import pbot


@pbot.on_message(filters.private & filters.media)
async def media_filter(bot, update):
    message = await update.reply_text(
        text="`Processing...`", quote=True, disable_web_page_preview=True
    )
    try:
        await message.edit_text(text="`Downloading...`", disable_web_page_preview=True)
        media = await update.download()
        await message.edit_text(text="`Uploading...`", disable_web_page_preview=True)
        response = pixeldrain.upload_file(media)
        status_code = response.status_code
        data = response.json()
        try:
            os.remove(media)
        except:
            pass
        await message.edit_text(
            text="`Uploaded Successfully!`", disable_web_page_preview=True
        )
        if data["success"] is False:
            await message.edit_text(
                text=f"**Error {status_code}:-** `I can't fetch information of your file.`",
                disable_web_page_preview=True,
            )
            return
    except Exception as error:
        await message.edit_text(
            text=f"Error :- <code>{error}</code>", disable_web_page_preview=True
        )
        return
    text = f"**File Name:** `{data['name']}`" + "\n"
    text += f"**Download Page:** `https://pixeldrain.com/u/{data['id']}`" + "\n"
    text += (
        f"**Direct Download Link:** `https://pixeldrain.com/api/file/{data['id']}`"
        + "\n"
    )
    text += f"**Upload Date:** `{data['date_upload']}`" + "\n"
    text += f"**Last View Date:** `{data['date_last_view']}`" + "\n"
    text += f"**Size:** `{data['size']}`" + "\n"
    text += f"**Total Views:** `{data['views']}`" + "\n"
    text += f"**Bandwidth Used:** `{data['bandwidth_used']}`" + "\n"
    text += f"**Mime Type:** `{data['mime_type']}`"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Open Link",
                    url=f"https://pixeldrain.com/api/file/{data['id']}",
                ),
                InlineKeyboardButton(
                    text="Share Link",
                    url=f"https://telegram.me/share/url?url=https://pixeldrain.com/api/file/{data['id']}",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Support", url="https://telegram.me/idzeroidsupport"
                )
            ],
        ]
    )
    await message.edit_text(
        text=text, reply_markup=reply_markup, disable_web_page_preview=True
    )
