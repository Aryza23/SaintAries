from pyrogram import filters

from aries import arq
from aries import pbot as app

ARQ_API_URL = "https://grambuilders.tech"


@app.on_message(filters.command("arq"))
async def arq_stats(_, message):
    data = await arq.stats()
    if not data.ok:
        return await message.reply_text(data.result)
    data = data.result
    uptime = data.uptime
    requests = data.requests
    cpu = data.cpu
    server_mem = data.memory.server
    api_mem = data.memory.api
    disk = data.disk
    platform = data.platform
    python_version = data.python
    users = data.users
    bot = data.bot
    statistics = f"""
📡 **Uptime:** `{uptime}`
🔘 **Requests Since Uptime:** `{requests}`
🔘 **CPU:** `{cpu}`
🔘 **Memory:**
    ⇝ **Total Used:** `{server_mem}`
    ⇝ **API:** `{api_mem}`
🔘 **Disk:** `{disk}`
🔘 **Platform:** `{platform}`
🔘 **Python:** `{python_version}`
🔘 **Users:** `{users}`
🔘 **Bot:** {bot}
🔘 **Address:** {ARQ_API_URL}
**Powered By:** __@IdzXartez__🔥
"""
    await message.reply_text(statistics, disable_web_page_preview=True)
