import re, os
from telethon import events, Button, custom
from aries import IDZ, telethn as tbot
from aries.events import register
from sys import version as pyver
from motor import version as mongover
from pyrogram import __version__ as pyrover


PHOTO = "https://telegra.ph/file/b4704fdf82e7a46cc5b51.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
  aries = event.sender.first_name
  ARIES = "**Hello im Saint Aries** \n\n"
  ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
  ARIES += " ☬ ⌊ **Python :** `{pyver.split()[0]}`⌉\n\n"
  ARIES += " ☬ ⌊ **Pyrogram :** `{pyrover}`⌉\n\n"
  ARIES += " ☬ ⌊ **MongoDB :** `{mongover}`⌉\n\n"
  ARIES += " ☬ ⌊ **Platform :** `{sys.platform}` ⌉\n\n"
  ARIES += " ☬ ⌊ **My Lord** : [Artezid](https://t.me/{IDZ}) ☠⌉\n\n"
  ARIES += " ☬ ⌊ **Sαιητ λrιεs** ⌉\n\n"
  ARIES += " ☬ ⌊ **TELETHON : 6.6.6 Latest** ⌉\n\n"
  ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
  BUTTON = [[Button.url("Support", "https://t.me/IDZEROIDSUPPORT"), Button.url("Owner", "https://t.me/IdzXartez")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ARIES,  buttons=BUTTON)


__mod_name__ = "Alive"
