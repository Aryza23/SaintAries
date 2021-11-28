import random
import requests
from bs4 import BeautifulSoup as bs
from pyjokes import get_joke
from telethon.errors import ChatSendMediaForbiddenError

from telegram import Update, ParseMode
from telegram.ext import CallbackContext

import aries.modules.aries_strings as aries_strings
from aries import dispatcher
from aries.modules.disable import DisableAbleCommandHandler
from aries.events import register


@register(pattern="^/joke ?(.*)")
async def joke(event):
    await event.reply(get_joke())


@register(pattern="^/insult ?(.*)")
async def insult(event):
    m = await event.reply("Generating...")
    nl = "https://fungenerators.com/random/insult/new-age-insult/"
    ct = requests.get(nl).content
    bsc = bs(ct, "html.parser", from_encoding="utf-8")
    cm = bsc.find_all("h2")[0].text
    await m.edit(f"{cm}")


@register(pattern="url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.reply("Give some url")
        return
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.reply(
            "**Shortened url**==> {}\n**Given url**==> {}.".format(
                response_api, input_str
            ),
        )
    else:
        await event.reply("`Something went wrong. Please try again Later.`")


AD_STRINGS = (
    "_*kembali dengan versi terbaik, karna di sini aku masih menunggumu,masih tentang kamu*_",
    "_*healing terbaik jatuh kepada rebahan, jalan jalan dan makanan enak*_",
    "_*sorry I'm not a perfect person like you, also not arrogant like you,and it's not something that requires me to be jealous.*_",
    "_*maaf aku bukan orang yang sempurna sepertimu, juga tidak sombong sepertimu, dan itu bukan sesuatu yang mengharuskan saya untuk cemburu.*_",
)


def aries(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = (
        message.reply_to_message.reply_photo
        if message.reply_to_message
        else message.reply_photo
    )
    reply_photo(random.choice(aries_strings.ARIES_IMG))


def diaryaryza(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(random.choice(AD_STRINGS), parse_mode=ParseMode.MARKDOWN)


__help__ = """
 ❍ `/aries`*:* gives random aries media.
 ❍ `/asupan`*:* gives random asupan medi.
 ❍ `/chika`*:* gives random chika media.
 ❍ `/wibu`*:* gives random wibu media.
 ❍ `/apakah`*:* For ask question about someone with AI.
 ❍ `/diaryaryza`*:* Check Aja.
 ❍ `/apod`*:* Get Astronomy Picture of Day by NASA.
 ❍ `/devian` <search query> ; <no of pics> *:* Devian-Art Image Search.
 ❍ `/joke`*:* To get random joke.
 ❍ `/inslut`*:* Insult someone..
 ❍ `/url <long url>`*:* To get a shorten link of long link.
"""


ARIES_HANDLER = DisableAbleCommandHandler("aries", aries, run_async=True)
dispatcher.add_handler(ARIES_HANDLER)

DIARYARYZA_HANDLER = DisableAbleCommandHandler("diaryaryza", diaryaryza, run_async=True)
dispatcher.add_handler(DIARYARYZA_HANDLER)

__mod_name__ = "Aries Extras"


__command_list__ = ["aries", "diaryaryza"]
__handlers__ = [ARIES_HANDLER, DIARYARYZA_HANDLER]
