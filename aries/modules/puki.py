## credit moezilla 

from pyrogram.types import (
  Message, 
)
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
import re
from aries import pbot as kuki

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

  Kuki =   requests.get(f"https://kuki-api.tk/api/botname/ownername/message={msg}").json()

  Kuki =   requests.get(f"https://kuki-api.tk/api/message={msg}").json()

  idz = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(idz)
