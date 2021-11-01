import requests

from aries.events import register


@register(pattern="^/truth ?(.*)")
async def _(td):
    try:
        kuntul = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = f"**{kuntul['message']}**"
        return await td.reply(results)
    except Exception:
        await td.reply("`Sedang Bermasalah...`")


@register(pattern="^/dare ?(.*)")
async def _(dr):
    try:
        kuntul = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = f"**{kuntul['message']}**"
        return await dr.reply(results)
    except Exception:
        await dr.reply("`Sedang Bermasalah...`")
