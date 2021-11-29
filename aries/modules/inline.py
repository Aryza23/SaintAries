import traceback

from aries import pbot as app
from aries.utils.inlinefuncs import *
import aiohttp
import requests
from aries.modules.nhentai import nhentai_data
from aries.modules.anime import (
    airing_query,
    anime_query,
    character_query,
    manga_query,
    shorten,
    t,
    url,
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)


class AioHttp:
    @staticmethod
    async def get_json(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.text()

    @staticmethod
    async def get_raw(link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                return await resp.read()




__mod_name__ = "Inline"
__help__ = """See inline for help related to inline"""


@app.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.strip().lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func(__help__)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif text.split()[0] == "alive":
            answerss = await alive_function(answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif text.split()[0] == "tr":
            if len(text.split()) < 3:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Translator | tr [LANG] [TEXT]",
                    switch_pm_parameter="inline",
                )
            lang = text.split()[1]
            tex = text.split(None, 2)[2].strip()
            answerss = await translate_func(answers, lang, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "ud":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Urban Dictionary | ud [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await urban_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )
        elif text.split()[0] == "google":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Google Search | google [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await google_search_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )

        elif text.split()[0] == "wall":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Wallpapers Search | wall [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wall_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "torrent":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Torrent Search | torrent [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await torrent_func(answers, tex)
            await client.answer_inline_query(
                query.id,
                results=answerss,
            )

        elif text.split()[0] == "yt":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="YouTube Search | yt [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await youtube_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss)

        elif text.split()[0] == "lyrics":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Lyrics Search | lyrics [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await lyrics_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss)

        elif text.split()[0] == "search":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Global Message Search. | search [QUERY]",
                    switch_pm_parameter="inline",
                )
            user_id = query.from_user.id
            tex = text.split(None, 1)[1].strip()
            answerss = await tg_search_func(answers, tex, user_id)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "music":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Music Search | music [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await music_inline_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "wiki":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Wikipedia | wiki [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await wiki_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "speedtest":
            answerss = await speedtest_init(query)
            return await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

        elif text.split()[0] == "pmpermit":
            user_id = query.from_user.id
            victim = text.split()[1]
            answerss = await pmpermit_func(answers, user_id, victim)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "ping":
            answerss = await ping_func(answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "ytmusic":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="YT Music | ytmusic [url]",
                    switch_pm_parameter="inline",
                )
            tex = query.query.split(None, 1)[1].strip()
            answerss = await yt_music_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "info":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="User Info | info [USERNAME|ID]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await info_inline_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "tmdb":
            if len(text.split()) < 2:
                answerss = await tmdb_func(answers, "")
                return await client.answer_inline_query(
                    query.id,
                    results=answerss,
                    switch_pm_text="TMDB Search | tmdb [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split()[1].strip()
            answerss = await tmdb_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "image":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    is_gallery=True,
                    switch_pm_text="Image Search | image [QUERY]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await image_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=3600
            )

        elif text.split()[0] == "exec":
            await execute_code(query)

        elif text.strip() == "tasks":
            user_id = query.from_user.id
            answerss = await task_inline_func(user_id)
            await client.answer_inline_query(query.id, results=answerss, cache_time=1)

    elif len(txt) != 0 and txt[0] == "nhentai":
        if len(txt) == 1:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="Enter nHentai ID",
                switch_pm_parameter="start",
            )
            return
        squery = string.split(None, 1)[1]
        n_title, tags, artist, total_pages, post_url, cover_image = nhentai_data(squery)
        reply_message = f"<code>{n_title}</code>\n\n<b>Tags:</b>\n{tags}\n<b>Artists:</b>\n{artist}\n<b>Pages:</b>\n{total_pages}"
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultArticle(
                    title=n_title,
                    input_message_content=InputTextMessageContent(reply_message),
                    description=tags,
                    thumb_url=cover_image,
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Read Here", url=post_url)]]
                    ),
                )
            ],
            cache_time=1,
        )
    elif len(txt) != 0 and txt[0] == "anime":
        if len(txt) == 1:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="Search an Anime",
                switch_pm_parameter="start",
            )
            return
        search = string.split(None, 1)[1]
        variables = {"search": search}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, json={"query": anime_query, "variables": variables}
            ) as resp:
                r = await resp.json()
                json = r["data"].get("Media", None)
                if json:
                    mal_id = int(json.get("idMal"))
                    msg = f"**{json['title']['romaji']}** (`{json['title']['native']}`)\n**Type**: {json['format']}\n**Status**: {json['status']}\n**Episodes**: {json.get('episodes', 'N/A')}\n**Duration**: {json.get('duration', 'N/A')} Per Ep.\n**Score**: {json['averageScore']}\n**Genres**: `"
                    for x in json["genres"]:
                        msg += f"{x}, "
                    msg = msg[:-2] + "`\n"
                    msg += "**Studios**: `"
                    for x in json["studios"]["nodes"]:
                        msg += f"{x['name']}, "
                    msg = msg[:-2] + "`\n"
                    info = json.get("siteUrl")
                    mal_link = f"https://myanimelist.net/anime/{mal_id}"
                    trailer = json.get("trailer", None)
                    if trailer:
                        trailer_id = trailer.get("id", None)
                        site = trailer.get("site", None)
                        if site == "youtube":
                            trailer = "https://youtu.be/" + trailer_id
                    description = (
                        json.get("description", "N/A")
                        .replace("<i>", "")
                        .replace("</i>", "")
                        .replace("<br>", "")
                    )
                    msg += shorten(description, info)
                    image = info.replace("anilist.co/anime/", "img.anili.st/media/")
                    if trailer:
                        buttons = [
                            [
                                InlineKeyboardButton("Anilist", url=info),
                                InlineKeyboardButton("MAL", url=mal_link),
                            ],
                            [InlineKeyboardButton("Trailer 🎬", url=trailer)],
                        ]
                    else:
                        buttons = [
                            [
                                InlineKeyboardButton("Anilist", url=info),
                                InlineKeyboardButton("MAL", url=mal_link),
                            ]
                        ]
                    if image:
                        answers.append(
                            InlineQueryResultPhoto(
                                caption=msg,
                                photo_url=image,
                                parse_mode="markdown",
                                title=f"{json['title']['romaji']}",
                                description=f"{json['format']} | {json.get('episodes', 'N/A')} Episode{'s' if len(str(json.get('episodes'))) > 1 else ''}",
                                reply_markup=InlineKeyboardMarkup(buttons),
                            )
                        )
                    else:
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{json['title']['romaji']}",
                                description=f"{json['format']} | {json.get('episodes', 'N/A')} Episode{'s' if len(str(json.get('episodes'))) > 1 else ''}",
                                input_message_content=InputTextMessageContent(
                                    msg, parse_mode="md", disable_web_page_preview=True
                                ),
                                reply_markup=InlineKeyboardMarkup(buttons),
                            )
                        )
        await client.answer_inline_query(
            query.id, results=answers, cache_time=0, is_gallery=False
        )
    elif len(txt) != 0 and txt[0] == "manga":
        if len(txt) == 1:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="Search a Manga",
                switch_pm_parameter="start",
            )
            return
        search = string.split(None, 1)[1]
        variables = {"search": search}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, json={"query": manga_query, "variables": variables}
            ) as resp:
                r = await resp.json()
                json = r["data"].get("Media", None)
                if json:
                    msg = f"**{json['title']['romaji']}** (`{json['title']['native']}`)\n**Status**: {json['status']}\n**Year**: {json['startDate']['year']}\n**Score**: {json['averageScore']}\n**Genres**: `"
                    for x in json["genres"]:
                        msg += f"{x}, "
                    msg = msg[:-2] + "`\n"
                    description = (
                        json.get("description", "N/A")
                        .replace("<i>", "")
                        .replace("</i>", "")
                        .replace("<br>", "")
                    )
                    info = json.get("siteUrl")
                    if info:
                        buttons = InlineKeyboardMarkup(
                            [[InlineKeyboardButton("More Info", url=info)]]
                        )
                    else:
                        buttons = None
                    msg += shorten(description, info)
                    banner_url = json.get("bannerImage")
                    if banner_url:
                        answers.append(
                            InlineQueryResultPhoto(
                                caption=msg,
                                photo_url=banner_url,
                                parse_mode="markdown",
                                title=f"{json['title']['romaji']}",
                                description=f"{json['startDate']['year']}",
                                reply_markup=buttons,
                            )
                        )
                    else:
                        answers.append(
                            InlineQueryResultArticle(
                                title=f"{json['title']['romaji']}",
                                description=f"{json['averageScore']}",
                                input_message_content=InputTextMessageContent(
                                    msg,
                                    parse_mode="markdown",
                                    disable_web_page_preview=True,
                                ),
                                reply_markup=buttons,
                            )
                        )
        await client.answer_inline_query(
            query.id, results=answers, cache_time=0, is_gallery=False
        )
    elif len(txt) != 0 and txt[0] == "airing":
        if len(txt) == 1:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="Get the Airing Status",
                switch_pm_parameter="start",
            )
            return
        search = string.split(None, 1)[1]
        variables = {"search": search}
        response = requests.post(
            url, json={"query": airing_query, "variables": variables}
        ).json()["data"]["Media"]
        info = response["siteUrl"]
        if info:
            buttons = InlineKeyboardMarkup(
                [[InlineKeyboardButton("More Info", url=info)]]
            )
        else:
            buttons = None
        image = info.replace("anilist.co/anime/", "img.anili.st/media/")
        if image:
            thumb = image
        else:
            thumb = None
        ms_g = f"**Name**: **{response['title']['romaji']}**(`{response['title']['native']}`)\n**ID**: `{response['id']}`"
        if response["nextAiringEpisode"]:
            airing_time = response["nextAiringEpisode"]["timeUntilAiring"] * 1000
            airing_time_final = t(airing_time)
            in_des = f"Episode {response['nextAiringEpisode']['episode']} Airing in {airing_time_final}"
            ms_g += f"\n**Episode**: `{response['nextAiringEpisode']['episode']}`\n**Airing In**: `{airing_time_final}`"
        else:
            in_des = "N/A"
            ms_g += f"\n**Episode**: `{response['episodes']}`\n**Status**: `N/A`"
        answers.append(
            InlineQueryResultArticle(
                title=f"{response['title']['romaji']}",
                description=f"{in_des}",
                input_message_content=InputTextMessageContent(
                    f"{ms_g}[⁠ ⁠]({image})",
                    parse_mode="markdown",
                    disable_web_page_preview=False,
                ),
                reply_markup=buttons,
                thumb_url=thumb,
            )
        )
        await client.answer_inline_query(
            query.id, results=answers, cache_time=0, is_gallery=False
        )
    elif len(txt) != 0 and txt[0] == "char":
        if len(txt) == 1:
            await client.answer_inline_query(
                query.id,
                results=answers,
                switch_pm_text="Get Character Info",
                switch_pm_parameter="start",
            )
            return
        search = string.split(None, 1)[1]
        variables = {"query": search}
        json = requests.post(
            url, json={"query": character_query, "variables": variables}
        ).json()["data"]["Character"]
        if json:
            ms_g = f"**{json.get('name').get('full')}**\nFavourites: {json['favourites']}\n"
            description = f"{json['description']}"
            site_url = json.get("siteUrl")
            ms_g += shorten(description, site_url)
            image = json.get("image", None)
            if image:
                image = image.get("large")
                answers.append(
                    InlineQueryResultPhoto(
                        caption=ms_g,
                        photo_url=image,
                        parse_mode="markdown",
                        title=f"{json.get('name').get('full')}",
                        description=f"❤️ {json['favourites']}",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("More Info", url=site_url)]]
                        ),
                    )
                )
            else:
                answers.append(
                    InlineQueryResultArticle(
                        title=f"{json.get('name').get('full')}",
                        description=f"{json['favourites']}",
                        input_message_content=InputTextMessageContent(
                            ms_g, parse_mode="markdown", disable_web_page_preview=True
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("More Info", url=site_url)]]
                        ),
                    )
                )
            await client.answer_inline_query(
                query.id, results=answers, cache_time=0, is_gallery=False
            )


    except Exception as e:
        e = traceback.format_exc()
        print(e, " InLine")
