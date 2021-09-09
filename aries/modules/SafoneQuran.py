import telebot
from telebot import types
import urllib.request
import time
import json
import os
from config import TOKEN
import logging

logging.basicConfig(filename="bot.log", format="%(asctime)s - %(levelname)s - %(message)s",
                        datefmt="%Y/%m/%d %I:%M:%S %p", level=0)
error_img = "https://telegra.ph/file/0d8baecfc982586bdec75.jpg"

BOT = telebot.TeleBot(f"{TOKEN}")

PAGES_URL = "http://mp3quran.net/api/quran_pages_arabic/"
with open('./messages.json', 'r') as j:
    messages = json.load(j)


def get_page(page_number, is_start):
    page_number = page_number if page_number > 1 and page_number < 604 else 604 if page_number < 1 else 1
    page_number = f"{'00' if page_number < 10 else '0' if page_number < 100 else ''}{page_number}"
    page_url = None if is_start else f"{PAGES_URL}{page_number}.png"
    return int(page_number), page_url

def send_page(user_id, first_name, chat_id, 
                message_id, page_number, is_start=False, 
                    send=False, with_markup=True):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton
    page_number, page_url= get_page(page_number, is_start)
    next_button = button(text="▶️Next", callback_data=f"{page_number + 1} {user_id} {first_name}")\
                    if with_markup else None
    back_button = button(text="◀️Previously", callback_data=f"{page_number - 1} {user_id} {first_name}")\
                    if with_markup else None
    start_button = button(text="Opening the Qur'an🕋", callback_data=f"{1} {user_id} {first_name}")\
                    if with_markup else None
    buttons_list = [start_button] if is_start else [back_button, next_button]\
                    if with_markup else []
    markup.add(*buttons_list)
    if is_start or send:
        BOT.send_photo(chat_id, page_url if page_url else open('./img/start_img.jpg', 'rb'),
                        reply_to_message_id=message_id,reply_markup=markup if with_markup else None,
                            caption=messages.get('start') if is_start else None)
    else:
        urllib.request.urlretrieve(page_url, f"{page_number}.png")
        with open(f"{page_number}.png", 'rb') as page:
            BOT.edit_message_media(types.InputMediaPhoto(page), chat_id, message_id, 
                                        reply_markup=markup if with_markup else None)
        os.remove(f"{page_number}.png")

def open_page(text, user_id, first_name, chat_id, 
                message_id, with_markup):
    s_text = text.split()
    user_info = [user_id, first_name, chat_id, message_id]
    if len(s_text) > 2 and s_text[2].isnumeric():
        page_number = int(s_text[2])
        if page_number > 0 and page_number < 604:
            send_page(*user_info, 
                        page_number, send=True, with_markup=with_markup)
        else:
            raise Exception("The number of pages of the Qur'an are 604")
    else:
        raise Exception("Please enter page number Example:\n%s 10" % (' '.join(s_text[:2])))

def get_info(ob):
    if ob.__class__ == types.Message:
        message_id = ob.id
        chat_id = ob.chat.id
    else:
        message_id = ob.message.id
        chat_id = ob.message.chat.id
    user_id = ob.from_user.id
    first_name = ob.from_user.first_name
    return [user_id, first_name, chat_id, message_id]


@BOT.message_handler(commands=['start', 'help'])
def command_handler(message):
    text = str(message.text)
    user_info = get_info(message)
    if text.startswith(('/start')):
        send_page(*user_info,
                    page_number=1, is_start=True)
    elif text.startswith('/help'):
        BOT.reply_to(message, messages.get('help'))

@BOT.message_handler(func=lambda msg:True, content_types=['text'])
def message_handler(message):
    text = str(message.text)
    user_info = get_info(message)
    if text.startswith("/open"):
        send_page(*user_info,
                    page_number=1, send=True)
    elif text.startswith(('open page', 'take the page')):
        try:
            open_page(text, *user_info, with_markup= not text.startswith(('take the page')))
        except Exception as err:
            BOT.reply_to(message, err)
    elif text in ['/repo']:
        BOT.reply_to(message, "If you want to make your own bot, bro? repo\nhttps://github.com/Achu2234/TelegramQuranReader")

@BOT.callback_query_handler(func=lambda call:True)
def query_handler(call):
    user_info = get_info(call)
    page_number, user_id, first_name = call.data.split(maxsplit=3)
    requester = call.from_user.id
    if int(user_id) == requester:
        send_page(*user_info, 
                    int(page_number), is_start=False)
    else:
        BOT.answer_callback_query(call.id, f"This Qur'an is for {first_name}")


while True:
    print("The boat is ready Join @AsmSafone")
    try:
        BOT.polling(none_stop=True, interval=0, timeout=0)
    except Exception as err:
        print(err)
        time.sleep(10)
