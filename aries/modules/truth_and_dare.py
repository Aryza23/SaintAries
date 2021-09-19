import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import aries.modules.truth_and_dare_string as truth_and_dare_string
from aries import dispatcher
from aries.modules.disable import DisableAbleCommandHandler


@run_async
def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


@run_async
def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)


dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
