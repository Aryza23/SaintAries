import random

from telegram import Update
from telegram.ext import CallbackContext

import aries.modules.aries_strings as aries_strings
from aries import dispatcher
from aries.modules.disable import DisableAbleCommandHandler

AD_STRINGS = (
    "_kembali dengan versi terbaik, karna di sini aku masih menunggumu,masih tentang kamu_",
    "_healing terbaik jatuh kepada rebahan, jalan jalan dan makanan enak_",
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
 ❍ `/aries`*:* gives random aries media
 ❍ `/asupan`*:* gives random asupan medi
 ❍ `/chika`*:* gives random chika media
 ❍ `/apakah`*:* For ask question about someone with AI
 ❍ `/diaryaryza`*:* Check Aja 
"""
ARIES_HANDLER = DisableAbleCommandHandler("aries", aries, run_async=True)
dispatcher.add_handler(ARIES_HANDLER)

DIARYARYZA_HANDLER = DisableAbleCommandHandler("diaryaryza", diaryaryza, run_async=True)
dispatcher.add_handler(DIARYARYZA_HANDLER)

__mod_name__ = "Aries fun"


__command_list__ = ["aries", "diaryaryza"]
__handlers__ = [ARIES_HANDLER, DIARYARYZA_HANDLER]
