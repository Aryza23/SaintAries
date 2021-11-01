# Copyright 2021 ©
# Modul Create by https://t.me/xflicks | Github = https://github.com/FeriEXP
# Yang remove cacat

import os
import urllib

import aiohttp
import requests
from pyrogram import filters

from aries import TEMP_DOWNLOAD_DIRECTORY, pbot


@pbot.on_message(filters.command("bugil"))
async def boobs(client, message):
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await message.reply_text("**Mencari Gambar Feri Lagi Bugil**")
    await a.edit("`Mengirim...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await client.send_photo(
        message.chat.id, pic_loc, caption="**Sange boleh, Goblok jangan**"
    )
    os.remove(pic_loc)
    await a.delete()


@pbot.on_message(filters.command("memes"))
async def memes(client, message):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            "https://meme-api.herokuapp.com/gimme/wholesomememes"
        ) as resp:
            r = await resp.json()
            await message.reply_photo(r["url"], caption=r["title"])
