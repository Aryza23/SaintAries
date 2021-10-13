# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Remove-BG-Bot/blob/main/LICENSE


import os
import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aries import pbot
from aries impot TEMP_DOWNLOAD_DIRECTORY as PATH

REMOVEBG_API = "icujRMB7cEDtbjUXow5Xw1up"
UNSCREEN_API = "mR7UnVPVRbV235iK8s5jk7vU"

ERROR_BUTTONS = InlineKeyboardMarkup(
        [
            InlineKeyboardButton("Support", url=f"https://t.me/idzeroidsupport")
        ]
    )



@pbot.on_message(filters.private & filters.command(["rmbg"]))
async def remove_background(bot, update):
    if not REMOVEBG_API:
        await update.reply_text(
            text="Error :- Remove BG Api is error",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )
        return
    await update.reply_chat_action("typing")
    message = await update.reply_text(
        text="Processing",
        quote=True,
        disable_web_page_preview=True
    )
    if update and update.media:
        new_file = PATH + str(update.from_user.id) + "/"
        if update.photo or (update.document and "image" in update.document.mime_type):
            new_file_name = new_file + "no_bg.png"
            file = await update.download(PATH+str(update.from_user.id))
            await message.edit_text(
                text="Photo downloaded successfully. Now removing background.",
                disable_web_page_preview=True
            )
            new_image = removebg_image(file)
            if new_image.status_code == 200:
                with open(new_file_name, "wb") as image:
                    image.write(new_image.content)
            else:
                await update.reply_text(
                    text="API is error.",
                    quote=True,
                    reply_markup=ERROR_BUTTONS
                )
                return
            await update.reply_chat_action("upload_photo")
            try:
                await update.reply_document(
                    document=new_file_name,
                    quote=True
                )
                await message.delete()
                try:
                    os.remove(file)
                except:
                    pass
            except Exception as error:
                print(error)
                await message.edit_text(
                    text="Something went wrong! May be API limits.",
                    disable_web_page_preview=True,
                    reply_markup=ERROR_BUTTONS
                ) 
    else:
        await message.edit_text(
            text="Media not supported",
            disable_web_page_preview=True,
            reply_markup=ERROR_BUTTONS
        )


def removebg_image(file):
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(file, "rb")},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVEBG_API}
    )


def removebg_video(file):
    return requests.post(
        "https://api.unscreen.com/v1.0/videos",
        files={"video_file": open(file, "rb")},
        headers={"X-Api-Key": UNSCREEN_API}
    )



