# Copyright (C) 2021 Bian Sepang
# All Rights Reserved.
# Recode Made by: https://github.com/FeriEXP


import nekos
from aries.events import register
arguments = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "goose",
    "baka",
    "woof",
    "kemonomimi",
    "smug",
]


@register(pattern="^/nekos ?(.*)")
async def nekos_img(event):
    args = event.pattern_match.group(1)
    if not args or args not in arguments:
        return await event.reply("type `.help nekos` to see available arguments.")
    anos = await event.reply("`Fetching from nekos...`")
    pic = nekos.img(args)
    await event.client.send_file(event.chat_id,pic)
    await anos.delete()
