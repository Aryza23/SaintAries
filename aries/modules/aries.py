import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import aries.modules.aries_strings as aries_strings
from aries import dispatcher
from aries.modules.disable import DisableAbleCommandHandler
from aries.modules.helper_funcs.chat_status import (is_user_admin)
from aries.modules.helper_funcs.extraction import extract_user

@run_async
def aries(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(aries_strings.ARIES_IMG))

__help__ = """
 • `/aries`*:* gives random aries media
 
"""
ARIES_HANDLER = DisableAbleCommandHandler("aries", aries)

dispatcher.add_handler(ARIES_HANDLER)

__mod_name__ = "Aries"
__command_list__ = [
    "aries"
]
__handlers__ = [
    ARIES_HANDLER
]
