from telethon import events, Button, custom
import re, os
from aries import IDZ, telethn as tbot
from aries.events import register

PHOTO = "https://telegra.ph/file/2b1756a57e11004461751.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
  aries = event.sender.first_name
  ARIES = "**Heya im Saint Aries** \n\n"
  ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
  ARIES += " ☬ ⌊ **Saint OS : 3.8 LATEST** ⌉\n\n"
  ARIES += f" ☬ ⌊ **My Lord** : @{IDZ} ☠⌉\n\n"
  ARIES += " ☬ ⌊ **Sαιητ λrιεs** ⌉\n\n"
  ARIES += " ☬ ⌊ **TELETHON : 1.19.5 LATEST** ⌉\n\n"
  ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
  BUTTON = [[Button.url("☠Support☠", "https://t.me/IDZEROIDSUPPORT"), Button.url("☠Channel☠", "https://t.me/IDZEROID")]]
  BUTTON += [[custom.Button.inline("REPOSITORY", data="http://github.com/idzero23")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ARIES,  buttons=BUTTON)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF ARIES OFFICIAL", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/idzero23/SaintAries")]])


__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive"
