from telethon import events, Button, custom
import re, os
from aries.events import register
from aries import telethn as tbot
from aries import telethn as tgbot
PHOTO = "https://telegra.ph/file/2b1756a57e11004461751.jpg"
@register(pattern=("/alive"))
async def awake(event):
  aries = event.sender.first_name
  ARIES = "HELLO THIS IS GRAND OFFICIAL \n\n"
  ARIES += "ALL SYSTEM WORKING PROPERLY\n\n"
  ARIES += "GRAND OS : 3.8 LATEST\n\n"
  ARIES += f"MY MASTER {aries} ☺️\n\n"
  ARIES += "FULLY UPDATED\n\n"
  ARIES += "TELETHON : 1.19.5 LATEST\n\n"
  ARIES += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/IdzXartez"), Button.url("DEVLOPER", "https://t.me/IdzXartez")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="ARIES")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=ARIES,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ARIES")))
async def callback_query_handler(event):
  ARIES = [[Button.url("REPO-ARIES", "https://github.com/idzero23/SaintAries"), Button.url("GITHUB", "https://github.com/idzero23")]]
  ARIES +=[[Button.url("SUPPORT CHANNEL", "https://t.me/IDZEROID"), Button.url("SUPPORT GROUP", "https://t.me/IDZEROIDSUPPORT")]]
  ARIES +=[[custom.Button.inline("ALIVE", data="ARIES")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=ARIES)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ARIES")))
async def callback_query_handler(event):
  global PHOTO
  aries = event.sender.first_name
  ARIES = "HELLO THIS IS GRAND OFFICIAL \n\n"
  ARIES += "ALL SYSTEM WORKING PROPERLY\n\n"
  ARIES += "GRAND OS : 3.8 LATEST\n\n"
  ARIES += f"MY MASTER {aries} ☺️\n\n"
  ARIES += "FULLY UPDATED BOT\n\n"
  ARIES += "TELETHON : 1.19.5 LATEST\n\n"
  ARIES += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/IdzXartez"), Button.url("DEVLOPER", "https://t.me/IdzXartez")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="ARIES")]]
  await event.edit(text=ARIES, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF GRAND OFFICIAL", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/idzero23/SaintAries")]])


__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive"
