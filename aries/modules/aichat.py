# Copyright (C) 2021 MoeZilla

# This file is part of Ie (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import os
import html
import requests
import aries.modules.sql.kuki_sql as sql

from time import sleep
from telegram import ParseMode
from aries import dispatcher, updater, SUPPORT_CHAT
from aries.modules.log_channel import gloggable
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, run_async, CallbackContext, MessageHandler, Filters
from aries.modules.helper_funcs.filters import CustomFilters
from aries.modules.helper_funcs.chat_status import user_admin
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown

@user_admin
@gloggable
def add_chat(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user
    is_kuki = sql.is_kuki(chat.id)
    if not is_kuki:
        sql.set_kuki(chat.id)
        msg.reply_text("Aries AI successfully enabled for this chat!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"AI_ENABLED\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message
    msg.reply_text("Aries AI is already enabled for this chat!")
    return ""


@user_admin
@gloggable
def rem_chat(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    is_kuki = sql.is_kuki(chat.id)
    if not is_kuki:
        msg.reply_text("Aries AI isn't enabled here in the first place!")
        return ""
    sql.rem_kuki(chat.id)
    msg.reply_text("Aries AI disabled successfully!")
    message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"AI_DISABLED\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
    )
    return message
 



def kuki_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "Aries":
        return True
    if reply_message:
        if reply_message.from_user.id == context.bot.get_me().id:
            return True
    else:
        return False
        

def aichat(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
	
    if message.text and not message.document:
        if not kuki_message(context, message):
            return
        Message = message.text
        bot.send_chat_action(chat_id, action="typing")
        kukiurl = requests.get('https://kuki-api.tk/api/Raiden/moezilla/message='+Message)
        Kukiurl = requests.get('https://kuki-api.tk/api/message='+Message)
        Kuki = json.loads(kukiurl.text)
        kuki = Kuki['reply']
        sleep(0.3)
        message.reply_text(kuki, timeout=60)

def list_all_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_kuki_chats()
    text = "<b>KUKI-Enabled Chats</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title if x.title else x.first_name
            text += f"• <code>{name}</code>\n"
        except BadRequest:
            sql.rem_kuki(*chat)
        except Unauthorized:
            sql.rem_kuki(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")
   

__help__ = """

"""

__mod_name__ = "Ai Chat"


__help__ = """
Chatbot utilizes the Kuki and allows aries to talk and provides a more interactive group chat experience.

*Commands:* 
*Admins only:*
   ➢ `addchat`*:* Enables Chatbot mode in the chat.
   ➢ `rmchat`*:* Disables Chatbot mode in the chat.
   
Reports bugs at Kuki-api.tk
*Powered by ItelAi* (https://github/itelai) from @KukiUpdates
"""

__mod_name__ = "Ai Chat"

ADD_CHAT_HANDLER = CommandHandler("addchat", add_chat)
REMOVE_CHAT_HANDLER = CommandHandler("rmchat", rem_chat)
AICHAT_HANDLER = MessageHandler(
    Filters.text & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!")
                    & ~Filters.regex(r"^\/")), aichat)
LIST_ALL_CHATS_HANDLER = CommandHandler(
    "allchats", list_all_chats, filters=CustomFilters.dev_filter)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(REMOVE_CHAT_HANDLER)
dispatcher.add_handler(LIST_ALL_CHATS_HANDLER)
dispatcher.add_handler(AICHAT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    REMOVE_CHAT_HANDLER,
    LIST_ALL_CHATS_HANDLER,
    AICHAT_HANDLER,
]
