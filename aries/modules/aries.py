import random

from telegram import Update
from telegram.ext import CallbackContext

import aries.modules.aries_strings as aries_strings
from aries import dispatcher
from aries.modules.disable import DisableAbleCommandHandler


def aries(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = (
        message.reply_to_message.reply_photo
        if message.reply_to_message
        else message.reply_photo
    )
    reply_photo(random.choice(aries_strings.ARIES_IMG))


__help__ = """
 ❍ `/aries`*:* gives random aries media
 ❍ `/asupan`*:* gives random asupan medi
 ❍ `/chika`*:* gives random chika media
"""
ARIES_HANDLER = DisableAbleCommandHandler("aries", aries, run_async=True)

dispatcher.add_handler(ARIES_HANDLER)

__mod_name__ = "🔘 Aries fun"
__command_list__ = ["aries"]
__handlers__ = [ARIES_HANDLER]
