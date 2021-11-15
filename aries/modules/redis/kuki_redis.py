import ast as idz
from aries import REDIS_URL

try:
    idz.literal_eval(REDIS_URL.get("KUKIBOT"))
except BaseException:
    REDIS_URL.set("KUKIBOT", "[]")


def is_kuki(chat_id):
    chat = idz.literal_eval(REDIS_URL.get("KUKIBOT"))
    chat = list(chat)
    if chat_id in chat:
        return True
    return False


def set_kuki(chat_id):
    chat = idz.literal_eval(REDIS_URL.get("KUKIBOT"))
    chat = list(chat)
    if chat_id not in chat:
        chat.append(chat_id)
        REDIS_URL.set("KUKIBOT", str(chat))
    return


def rm_kuki(chat_id):
    chat = idz.literal_eval(REDIS_URL.get("KUKIBOT"))
    chat = list(chat)
    if chat_id in chat:
        chat.remove(chat_id)
        REDIS_URL.set("KUKIBOT", str(chat))
    return
