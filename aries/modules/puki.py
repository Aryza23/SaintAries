## credit moezilla 

from pyrogram.types import (
  Message, 
)
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
import re

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
TOKEN = os.environ.get("TOKEN", None) 
BOT_ID = os.environ.get("BOT_ID", None)


kuki = Client(
      "KukiBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=TOKEN,
)

@kuki.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kuki-api.tk/api/testeraichatbot/IdzXartez/message={msg}").json()

  Kuki =   requests.get(f"https://kuki-api.tk/api/message=hi").json()

  idz = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(idz)


messageprivate = '''
Hi, I'm Kuki Chat Bot 
'''

messagegroup = '''
⚡️
'''





@kuki.on_message(filters.command("start"))
async def start(_, message):
    self = await kuki.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Github", url="https://github.com/idzero23/ArtezidAI"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))



__mod_name__ = "PUKI"
