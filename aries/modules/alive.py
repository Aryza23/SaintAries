import re, os
from telethon import events, Button, custom
from aries import IDZ, telethn as tbot
from aries.events import register


PHOTO = "https://telegra.ph/file/b4704fdf82e7a46cc5b51.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    aries = event.sender.first_name
    ARIES = "**Hello im Saint Aries** \n\n"
    ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
    ARIES += " ☬ ⌊ **Python :** __3.9.7__ ⌉\n\n"
    ARIES += " ☬ ⌊ **Pyrogram :** __1.2.9__ ⌉\n\n"
    ARIES += " ☬ ⌊ **MongoDB :** __2.5.1__ ⌉\n\n"
    ARIES += " ☬ ⌊ **Platform :** __linux__ ⌉\n\n"
    ARIES += " ☬ ⌊ **My Lord** : [Artezid](https://t.me/{IDZ}) ☠⌉\n\n"
    ARIES += " ☬ ⌊ **Sαιητ λrιεs** ⌉\n\n"
    ARIES += " ☬ ⌊ **TELETHON : 6.6.6 Latest** ⌉\n\n"
    ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Support", "https://t.me/IDZEROIDSUPPORT"),
            Button.url("Owner", "https://t.me/IdzXartez"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=ARIES, buttons=BUTTON)


__mod_name__ = "Alive"
