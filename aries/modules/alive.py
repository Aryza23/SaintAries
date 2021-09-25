from telethon import events, Button, custom
import re, os
from aries import IDZ, telethn as tbot
from aries.events import register

PHOTO = "https://telegra.ph/file/b4704fdf82e7a46cc5b51.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
  aries = event.sender.first_name
  ARIES = "**Hello im Saint Aries** \n\n"
  ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
  ARIES += " ☬ ⌊ **Saint OS : 3.8 LATEST** ⌉\n\n"
  ARIES += f" ☬ ⌊ **My Lord** : [Artezid](https://t.me/{IDZ}) ☠⌉\n\n"
  ARIES += " ☬ ⌊ **Sαιητ λrιεs** ⌉\n\n"
  ARIES += " ☬ ⌊ **TELETHON : 1.19.5 LATEST** ⌉\n\n"
  ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
  BUTTON = [[Button.url("⌊Support⌉", "https://t.me/IDZEROIDSUPPORT"), Button.url("⌊Channel⌉", "https://t.me/IDZEROID")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ARIES,  buttons=BUTTON)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  REPOS ""REPO OF ARIES OFFICIAL"
  await tbot.send_file(event.chat, PHOTO, caption=REPOS, buttons=[[Button.url("⚜️REPO⚜️", "https://www.sukatoro.com/")]])


__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive"
