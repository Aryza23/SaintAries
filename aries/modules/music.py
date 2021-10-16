import asyncio
import io
import os
import time

import lyricsgenius
import requests
import wget
from pyrogram import filters
from pyrogram.types import Message
from tswift import Song
from youtube_dl import YoutubeDL
from youtubesearchpython import SearchVideos

from aries.conf import get_str_key
from aries.pyrogramee.pluginshelper import get_text, progress
from aries import pbot

GENIUS = "LstbAM4nzj2txUk2DGKh-PC0z6BxY1JYhMxMdj1NdRtmm7B7XYs0WcYBj4bFLK"

@pbot.on_message(filters.command(["vsong", "video"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` \n**Link :** `{mo}`"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


@pbot.on_message(filters.command(["music", "song", "lagu"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    if not urlissed:
        await client.send_message(
            message.chat.id,
            "Invalid Command Syntax, Please Check Help Menu To Know More!",
        )
        return
    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    sedlyf = wget.download(kekme)
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "720",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
    except Exception as e:
        await pablo.edit(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    capy = f"**Song Name :** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` \n**Link :** `{mo}` \n**Powered By :**__@IdzXartez__"
    file_stark = f"{ytdl_data['id']}.mp3"
    await client.send_audio(
        message.chat.id,
        audio=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        title=str(ytdl_data["title"]),
        performer=str(ytdl_data["uploader"]),
        thumb=sedlyf,
        caption=capy,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


@pbot.on_message(filters.command(["deezer", "dsong"]))
async def deezer(client, message: Message):
    pablo = await client.send_message(message.chat.id, "Searching the song")
    sgname = get_text(message)
    if not sgname:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    link = f"https://api.deezer.com/search?q={sgname}&limit=1"
    dato = requests.get(url=link).json()
    match = dato.get("data")
    urlhp = match[0]
    urlp = urlhp.get("link")
    thums = urlhp["album"]["cover_big"]
    thum_f = wget.download(thums)
    polu = urlhp.get("artist")
    replo = urlp[29:]
    urlp = f"https://starkapi.herokuapp.com/deezer/{replo}"
    datto = requests.get(url=urlp).json()
    mus = datto.get("url")
    sname = f"{urlhp.get('title')}.mp3"
    doc = requests.get(mus)
    await client.send_chat_action(message.chat.id, "upload_audio")
    await pablo.edit("`Downloading Song From Deezer!`")
    with open(sname, "wb") as f:
        f.write(doc.content)
    c_time = time.time()
    await pablo.edit(f"`Downloaded {sname}! Now Uploading Song...`")
    await client.send_audio(
        message.chat.id,
        audio=open(sname, "rb"),
        duration=int(urlhp.get("duration")),
        title=str(urlhp.get("title")),
        performer=str(polu.get("name")),
        thumb=thum_f,
        progress=progress,
        progress_args=(pablo, c_time, f"`Uploading {sname} Song From Deezer!`", sname),
    )
    await client.send_chat_action(message.chat.id, "cancel")
    await pablo.delete()


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Lel, Didn't Get Time To Make New One So Used Plugin Made br @mrconfused and @sandy1709 dont edit credits


@pbot.on_message(filters.command(["lyric", "lyrics"]))
async def _(client, message):
    lel = await message.reply("Searching For Lyrics.....")
    query = message.text
    if not query:
        await lel.edit("`What I am Supposed to find `")
        return

    song = ""
    song = Song.find_song(query)
    if song:
        if song.lyrics:
            reply = song.format()
        else:
            reply = "Couldn't find any lyrics for that song! try with artist name along with song if still doesnt work try `.glyrics`"
    else:
        reply = "lyrics not found! try with artist name along with song if still doesnt work try `.glyrics`"

    if len(reply) > 4095:
        with io.BytesIO(str.encode(reply)) as out_file:
            out_file.name = "lyrics.text"
            await client.send_document(
                message.chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=query,
                reply_to_msg_id=message.message_id,
            )
            await lel.delete()
    else:
        await lel.edit(reply)  # edit or reply


@pbot.on_message(filters.command(["glyric", "glyrics"]))
async def lyrics(client, message):

    if r"-" in message.text:
        pass
    else:
        await message.reply(
            "`Error: please use '-' as divider for <artist> and <song>`\n"
            "eg: `.glyrics Nicki Minaj - Super Bass`"
        )
        return

    if GENIUS is None:
        await message.reply(
            "`Provide genius access token to config.py or Heroku Config first ok thx bye!`"
        )
    else:
        genius = lyricsgenius.Genius(GENIUS)
        try:
            args = message.text.split(".lyrics")[1].split("-")
            artist = args[0].strip(" ")
            song = args[1].strip(" ")
        except Exception:
            await message.reply("`Lel please provide artist and song names`")
            return

    if len(args) < 1:
        await message.reply("`Please provide artist and song names`")
        return

    lel = await message.reply(f"`Searching lyrics for {artist} - {song}...`")

    try:
        songs = genius.search_song(song, artist)
    except TypeError:
        songs = None

    if songs is None:
        await lel.edit(f"Song **{artist} - {song}** not found!")
        return
    if len(songs.lyrics) > 4096:
        await lel.edit("`Lyrics is too big, view the file to see it.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Search query: \n{artist} - {song}\n\n{songs.lyrics}")
        await client.send_document(
            message.chat.id,
            "lyrics.txt",
            reply_to_msg_id=message.message_id,
        )
        os.remove("lyrics.txt")
    else:
        await lel.edit(
            f"**Search query**: \n`{artist} - {song}`\n\n```{songs.lyrics}```"
        )
    return

