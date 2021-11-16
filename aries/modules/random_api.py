import requests
import random
from aries import telethn as tbot
from aries.events import register
import aries.modules.fun_strings as fun_strings

@register(pattern="^/apakah ?(.*)")
async def apakah(event)
    kontol = event.pattern_match.group(1)
    if not kontol:
        await event.reply("Example: /apakah (text)")
        return
    await event.reply(random.choice(fun_strings.APAKAH_STRINGS))


@register(pattern="^/asupan ?(.*)")
async def asupan(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        asupannya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, asupannya)
    except Exception:
        await event.reply("`Error 404 not found...`")


@register(pattern="^/chika ?(.*)")
async def chika(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        chikanya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, chikanya)
    except Exception:
        await event.reply("`Error 404 not found...`")


@register(pattern="^bocil ?(.*)")
async def bocil(event):
    try:
        resp = requests.get("https://feri-api.herokuapp.com/api/asupan/bocil").json()
        bocilnya = f"{resp['url']}"
        return await tbot.send_file(event.chat_id, bocilnya)
    except Exception:
        await event.reply("`Error 404 not found...`")
