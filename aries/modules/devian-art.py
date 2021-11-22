import random
import re

import requests
from bs4 import BeautifulSoup as bs

from aries.events import register

try:
    import aiofiles
    import aiohttp
except ImportError:
    import urllib

    aiohttp = None


async def download_file(link, name):
    """for files, without progress callback with aiohttp"""
    if not aiohttp:
        urllib.request.urlretrieve(link, name)
        return name
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as re_ses:
            file = await aiofiles.open(name, "wb")
            await file.write(await re_ses.read())
            await file.close()
    return name


@register(pattern="^/devian?(.*)")
async def downakd(e):
    match = e.pattern_match.group(1)
    if not match:
        return await e.reply("`Give Query to Search...`")
    Random = False
    if ";" in match:
        num = int(match.split(";")[1])
        if num == 1:
            Random = True
        match = match.split(";")[0]
    else:
        num = 5
    xd = await e.reply("`Processing...`")
    match = match.replace(" ", "+")
    link = "https://www.deviantart.com/search?q=" + match
    ct = requests.get(link).content
    st = bs(ct, "html.parser", from_encoding="utf-8")
    res = st.find_all("img", loading="lazy", src=re.compile("https://images-wixmp"))[
        :num
    ]
    if Random:
        res = [random.choice(res)]
    out = []
    num = 0
    for on in res:
        img = await download_file(on["src"], f"./downloads/{match}-{num}.jpg")
        num += 1
        out.append(img)
    if len(out) == 0:
        return await xd.edit("`No Results Found!`")
    await e.client.send_file(
        e.chat_id, out, caption=f"Uploaded {len(res)} Images\n", album=True
    )
    await xd.delete()
