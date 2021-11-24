from aries.modules.helper_funcs.decorators import idzcallback
from telegram import (
    ParseMode,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext


def fmt_md_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        (update.effective_chat.id, "md_help"),
        parse_mode=ParseMode.HTML,
    )


def fmt_filling_help(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        (update.effective_chat.id, "filling_help"),
        parse_mode=ParseMode.HTML,
    )


@idzcallback(pattern=r"fmt_help_")
def fmt_help(update: Update, context: CallbackContext):
    query = update.callback_query
    bot = context.bot
    help_info = query.data.split("fmt_help_")[1]
    if help_info == "md":
        help_text = (update.effective_chat.id, "md_help")
    elif help_info == "filling":
        help_text = (update.effective_chat.id, "filling_help")
    query.message.edit_text(
        text=help_text,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Back",
                        callback_data=f"help_module({__mod_name__.lower()})",
                    ),
                    InlineKeyboardButton(
                        text="Report Error", url="https://t.me/idzeroidsupport"
                    ),
                ]
            ]
        ),
    )
    bot.answer_callback_query(query.id)


__mod_name__ = "Formatting"

__mod_help__ = "test"

def get_help(chat):
    return [
        (chat, "formt_help_bse"),
        [
            InlineKeyboardButton(text="Markdown", callback_data="fmt_help_md"),
            InlineKeyboardButton(text="Filling", callback_data="fmt_help_filling"),
        ],
    ]
