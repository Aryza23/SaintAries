import requests
from aries.events import register
from aries import telethn as tbot


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
