# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• {i}devian <search query> ; <no of pics>
    Devian-Art Image Search.
"""

import random
import re

import requests
from bs4 import BeautifulSoup as bs
from aries import telethn as tbot
from aries.events import register
from aries import ubot

@register(pattern="^/devian ?(.*)")
async def _(event):
    match = event.pattern_match.group(1)
    if not match:
        return await event.reply("`Give Query to Search...`")
    Random = False
    if ";" in match:
        num = int(match.split(";")[1])
        if num == 1:
            Random = True
        match = match.split(";")[0]
    else:
        num = 5
    xd = await event.reply("`Processing...`")
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
        img = await ubot.download_media(
            on["src"], f"resources/downloads/{match}-{num}.jpg"
        )
        num += 1
        out.append(img)
    if len(out) == 0:
        return await xd.edit("`No Results Found!`")
    await tbot.send_file(
        event.chat_id, out, caption=f"Uploaded {len(res)} Images\n", album=True
    )
    await xd.delete()
