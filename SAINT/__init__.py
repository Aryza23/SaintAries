from aries.events import register as SAINTX23
from aries import telethn as bot
from aries import API_ID, API_HASH
from aries.events import *
from telethon import TelegramClient
from telethon.sessions import StringSession

import os
STRING_SESSION = os.environ.get("STRING_SESSION")
if STRING_SESSION:
    user = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
else:
     print ("please add StringSession var")

try:
     user.start()
except Exception as e:
     print(e)
