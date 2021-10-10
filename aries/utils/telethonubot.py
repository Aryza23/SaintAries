import sys
from telethon import TelegramClient
from telethon.sessions import StringSession
from aries.confing import get_int_key, get_str_key
from aries import STRING_SESSION

STRING_SESSION = get_str_key("STRING_SESSION", required=True)
API_ID = get_int_key("API_ID", required=True)
API_HASH = get_str_key("API_HASH", required=True)

ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
try:
    ubot.start()
except BaseException:
    print("Userbot Error ! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)
