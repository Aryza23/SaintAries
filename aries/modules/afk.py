import time

from telegram import MessageEntity
from telegram.error import BadRequest
from telegram.ext import Filters, MessageHandler

from aries import dispatcher, REDIS
from aries.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)
from aries.modules.helper_funcs.readable_time import get_readable_time
from aries.modules.redis.afk_redis import (
    start_afk,
    end_afk,
    is_user_afk,
    afk_reason,
)
from aries.modules.users import get_user_id

AFK_GROUP = 7
AFK_REPLY_GROUP = 8


def afk(update, _):
    message = update.effective_message
    args = message.text.split(None, 1)
    user = update.effective_user

    if not user:  # ignore channels
        return

    if user.id in [777000, 1087968824]:
        return

    start_afk_time = time.time()
    reason = args[1] if len(args) >= 2 else "none"
    start_afk(user.id, reason)
    REDIS.set(f"afk_time_{user.id}", start_afk_time)
    fname = user.first_name
    try:
        message.reply_text("{} is now AFK!".format(fname))
    except BadRequest:
        pass


def no_longer_afk(update, _):
    user = update.effective_user
    message = update.effective_message
    if not user:  # ignore channels
        return

    if not is_user_afk(user.id):  # Check if user is afk or not
        return
    end_afk_time = get_readable_time(
        (time.time() - float(REDIS.get(f"afk_time_{user.id}")))
    )
    REDIS.delete(f"afk_time_{user.id}")
    res = end_afk(user.id)
    if res:
        if message.new_chat_members:  # dont say msg
            return
        firstname = update.effective_user.first_name
        try:
            message.reply_text(
                "{} is back online!\nYou were away for: {}".format(
                    firstname, end_afk_time
                )
            )
        except BaseException:
            pass


def reply_afk(update, context):
    message = update.effective_message
    userc = update.effective_user
    userc_id = userc.id
    if message.entities and message.parse_entities(
        [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
    ):
        entities = message.parse_entities(
            [MessageEntity.TEXT_MENTION, MessageEntity.MENTION]
        )

        chk_users = []
        for ent in entities:
            if ent.type == MessageEntity.TEXT_MENTION:
                user_id = ent.user.id
                fst_name = ent.user.first_name

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

            elif ent.type == MessageEntity.MENTION:
                user_id = get_user_id(
                    message.text[ent.offset : ent.offset + ent.length]
                )
                if not user_id:
                    # Should never happen, since for a user to become AFK they must have spoken. Maybe changed username?
                    return

                if user_id in chk_users:
                    return
                chk_users.append(user_id)

                try:
                    chat = context.bot.get_chat(user_id)
                except BadRequest:
                    print(
                        "Error: Could not fetch userid {} for AFK module".format(
                            user_id
                        )
                    )
                    return
                fst_name = chat.first_name

            else:
                return

            check_afk(update, context, user_id, fst_name, userc_id)

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        fst_name = message.reply_to_message.from_user.first_name
        check_afk(update, context, user_id, fst_name, userc_id)


def check_afk(update, context, user_id: int, fst_name: int, userc_id: int):
    if is_user_afk(user_id):
        reason = afk_reason(user_id)
        since_afk = get_readable_time(
            (time.time() - float(REDIS.get(f"afk_time_{user_id}")))
        )
        if int(userc_id) == int(user_id):
            return
        if reason == "none":
            res = "{} is AFK!\nLast seen: {}".format(fst_name, since_afk)
        else:
            res = "{} is AFK!\nReason: {}\nLast seen: {}".format(
                fst_name, reason, since_afk
            )

        update.effective_message.reply_text(res)


def __gdpr__(user_id):
    end_afk(user_id)


__help__ = """
When marked as AFK, any mentions will be replied to with a message to say you're not available!

❍ /afk <reason>: Mark yourself as AFK.
❍ brb <reason>: Same as the afk command - but not a command.

An example of how to afk or brb:
`/afk dinner` or brb dinner.
"""

AFK_HANDLER = DisableAbleCommandHandler(
    "afk",
    afk,
    run_async=True,
)
AFK_REGEX_HANDLER = DisableAbleMessageHandler(
    Filters.regex("(?i)^brb"),
    afk,
    friendly="afk",
    run_async=True,
)
NO_AFK_HANDLER = MessageHandler(
    Filters.all & Filters.chat_type.groups,
    no_longer_afk,
    run_async=True,
)
AFK_REPLY_HANDLER = MessageHandler(
    Filters.all & Filters.chat_type.groups & ~Filters.update.edited_message,
    reply_afk,
    run_async=True,
)

dispatcher.add_handler(AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REGEX_HANDLER, AFK_GROUP)
dispatcher.add_handler(NO_AFK_HANDLER, AFK_GROUP)
dispatcher.add_handler(AFK_REPLY_HANDLER, AFK_REPLY_GROUP)

__mod_name__ = "🔘 AFK"
__command_list__ = ["afk"]
__handlers__ = [
    (AFK_HANDLER, AFK_GROUP),
    (AFK_REGEX_HANDLER, AFK_GROUP),
    (NO_AFK_HANDLER, AFK_GROUP),
    (AFK_REPLY_HANDLER, AFK_REPLY_GROUP),
]
