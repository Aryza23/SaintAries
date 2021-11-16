# credits @RoseLoverX
import asyncio
import os

from aries import OWNER_ID
from aries.events import register

water = "./aries/resources/Aries.jpg"


@register(pattern=r"^/send ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./aries/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        message_id = event.message.id
        await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
    else:
        await event.reply("No File Found!")


import asyncio
import os
from pathlib import Path

from aries.events import load_module


@register(pattern="^/install")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "aries/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.reply(
                    "Installed.... 👍\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                k = await event.reply(
                    "**Error!**\n⚠️Cannot Install! \n📂 File not supported \n Or Pre Installed Maybe..😁",
                )
                await asyncio.sleep(2)
                await k.delete()
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()


import asyncio
import os

from aries import OWNER_ID
from aries import telethn as tbot
from aries.events import register

opn = []


@register(pattern="/open")
async def _(event):
    xx = await event.reply("Processing...")
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        if a.media:
            b = await a.download_media()
            c = open(b, "r")
            d = c.read()
            c.close()
            n = 4096
            for bkl in range(0, len(d), n):
                opn.append(d[bkl : bkl + n])
            for bc in opn:
                await event.client.send_message(
                    event.chat_id,
                    f"{bc}",
                    reply_to=event.reply_to_msg_id,
                )
            await event.delete()
            opn.clear()
            os.remove(b)
            await xx.delete()
        else:
            return await event.reply("Reply to a readable file")
    else:
        return await event.reply("Reply to a readable file")


client = tbot
from pathlib import Path


@register(pattern="^/make ?(.*)")
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.reply("reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.reply("reply to text message as `.ttf <file name>`")
