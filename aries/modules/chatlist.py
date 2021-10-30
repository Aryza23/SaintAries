from io import BytesIO
from time import sleep

from telegram import Bot, Update, TelegramError
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, Filters, run_async

import aries.modules.sql.users_sql as sql

from aries import dispatcher, OWNER_ID, LOGGER, DEV_USERS
from aries.modules.helper_funcs.chat_status import sudo_plus, dev_plus

USERS_GROUP = 4
DEV_AND_MORE = DEV_USERS.append(int(OWNER_ID))


def get_user_id(username):
    # ensure valid userid
    if len(username) <= 5:
        return None

    if username.startswith('@'):
        username = username[1:]

    users = sql.get_userid_by_name(username)

    if not users:
        return None

    elif len(users) == 1:
        return users[0].user_id

    else:
        for user_obj in users:
            try:
                userdat = dispatcher.bot.get_chat(user_obj.user_id)
                if userdat.username == username:
                    return userdat.id

            except BadRequest as excp:
                if excp.message == 'Chat not found':
                    pass
                else:
                    LOGGER.exception("Error extracting user ID")

    return None




def log_user(bot: Bot, update: Update):
    chat = update.effective_chat
    msg = update.effective_message

    sql.update_user(msg.from_user.id,
                    msg.from_user.username,
                    chat.id,
                    chat.title)

    if msg.reply_to_message:
        sql.update_user(msg.reply_to_message.from_user.id,
                        msg.reply_to_message.from_user.username,
                        chat.id,
                        chat.title)

    if msg.forward_from:
        sql.update_user(msg.forward_from.id,
                        msg.forward_from.username)



@sudo_plus
def chats(bot: Bot, update: Update):

    all_chats = sql.get_all_chats() or []
    chatfile = 'List of chats.\n'
    for chat in all_chats:
        chatfile += f"{chat.chat_name} - ({chat.chat_id})\n"

    with BytesIO(str.encode(chatfile)) as output:
        output.name = "chatlist.txt"
        update.effective_message.reply_document(document=output, filename="chatlist.txt",
                                                caption="Here is the list of chats in my Hit List.")


def __stats__():
    return f"{sql.num_users()} users, across {sql.num_chats()} chats"


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


__help__ = ""  # no help string

USER_HANDLER = MessageHandler(Filters.all & Filters.chat_type.groups, log_user, run_async=True)
CHATLIST_HANDLER = CommandHandler("chatlist", chats, run_async=True)

dispatcher.add_handler(USER_HANDLER, USERS_GROUP)
dispatcher.add_handler(CHATLIST_HANDLER)

__mod_name__ = "chatlist"
__handlers__ = [(USER_HANDLER, USERS_GROUP), CHATLIST_HANDLER]
