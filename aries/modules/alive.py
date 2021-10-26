import re, os
from telethon import events, Button, custom
from aries import IDZ, telethn as tbot
from aries.events import register
from telethon import __version__ as telever
from telegram import __version__ as tgver
PHOTO = "https://telegra.ph/file/b4704fdf82e7a46cc5b51.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
  aries = event.sender.first_name
  ARIES = "**Hello im Saint Aries** \n\n"
  ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
  ARIES += " ☬ ⌊ **Telegram : {tgver}** ⌉\n\n"
  ARIES += f" ☬ ⌊ **My Lord** : [Artezid](https://t.me/{IDZ}) ☠⌉\n\n"
  ARIES += " ☬ ⌊ **Sαιητ λrιεs** ⌉\n\n"
  ARIES += " ☬ ⌊ **TELETHON : {telever}** ⌉\n\n"
  ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
  BUTTON = [[Button.url("⌊Support⌉", "https://t.me/IDZEROIDSUPPORT"), Button.url("⌊Channel⌉", "https://t.me/IDZEROID")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ARIES,  buttons=BUTTON)


__mod_name__ = "Alive"
