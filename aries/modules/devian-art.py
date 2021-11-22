import random
import re

import requests
from bs4 import BeautifulSoup as bs

from aries.events import register


@register(pattern="^/devian ?(.*)")
async def devian:
    match = devian.pattern_match.group(1)
    if not match:
        return await devian.reply("`Give Query to Search...`")
    Random = False
    if ";" in match:
        num = int(match.split(";")[1])
        if num == 1:
            Random = True
        match = match.split(";")[0]
    else:
        num = 5
    xd = await devian.reply("`Processing...`")
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
        img = await download_file(on["src"], f"resources/downloads/{match}-{num}.jpg")
        num += 1
        out.append(img)
    if len(out) == 0:
        return await xd.edit("`No Results Found!`")
    await devian.client.send_file(
        devian.chat_id, out, caption=f"Uploaded {len(res)} Images\n", album=True
    )
    await xd.delete()
