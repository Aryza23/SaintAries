from aries import telethn as bot
from aries import ubot
import asyncio
from telethon import events
from telethon.tl.types import (
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    InputMessagesFilterMusic,
    InputMessagesFilterVideo,
    InputMessagesFilterRoundVideo,
    InputMessagesFilterDocument,
    InputMessagesFilterUrl,
    InputMessagesFilterGif,
    InputMessagesFilterGeo,
    InputMessagesFilterContacts,
)


@bot.on(events.NewMessage(pattern="^/gstat$"))
async def fk(m):
    lol = await m.client.send_message(m.chat.id, "Connecting To The Database")
    al = str((await ubot.get_messages(m.chat_id, limit=0)).total)
    ph = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterPhotos()
            )
        ).total
    )
    vi = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterVideo()
            )
        ).total
    )
    mu = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterMusic()
            )
        ).total
    )
    vo = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterVideo()
            )
        ).total
    )
    vv = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterRoundVideo()
            )
        ).total
    )
    do = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterDocument()
            )
        ).total
    )
    urls = str(
        (
            await ubot.get_messages(m.chat_id, limit=0, filter=InputMessagesFilterUrl())
        ).total
    )
    gifs = str(
        (
            await ubot.get_messages(m.chat_id, limit=0, filter=InputMessagesFilterGif())
        ).total
    )
    geos = str(
        (
            await ubot.get_messages(m.chat_id, limit=0, filter=InputMessagesFilterGeo())
        ).total
    )
    cont = str(
        (
            await ubot.get_messages(
                m.chat_id, limit=0, filter=InputMessagesFilterContacts()
            )
        ).total
    )
    await asyncio.sleep(1)
    await lol.edit(
        (
            "✉️ Total Messages: {}\n"
            + "🖼 Total Photos: {}\n"
            + "📹 Total Video Messages: {}\n"
            + "🎵 Total music Messages : {}\n"
            + "🎶 Total Audio: {}\n"
            + "🎥 Total Videos: {}\n"
            + "📂 Total Files: {}\n"
            + "🔗 Total Links: {}\n"
            + "🎞 Total GIF: {}\n"
            + "🗺 Total Geo Messages: {}\n"
            + "👭 Total Contact files: {}"
        ).format(al, ph, vi, mu, vo, vv, do, urls, gifs, geos, cont)
    )
