import json

import requests
from telegram.ext import CommandHandler

from aries import dispatcher
from aries.modules.helper_funcs.alternate import send_message
from aries.modules.helper_funcs.chat_status import user_admin


@user_admin
def phone(update, context):

    args = update.effective_message.text.split(None, 1)
    information = args[1]
    number = information
    key = "fe65b94e78fc2e3234c1c6ed1b771abd"
    api = (
        "http://apilayer.net/api/validate?access_key="
        + key
        + "&number="
        + number
        + "&country_code=&format=1"
    )
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj["country_code"]
    country_name = obj["country_name"]
    location = obj["location"]
    carrier = obj["carrier"]
    line_type = obj["line_type"]
    validornot = obj["valid"]
    aa = "Valid: " + str(validornot)
    a = "Phone number: " + str(number)
    b = "Country: " + str(country_code)
    c = "Country Name: " + str(country_name)
    d = "Location: " + str(location)
    e = "Carrier: " + str(carrier)
    f = "Device: " + str(line_type)
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    send_message(update.effective_message, g)


PHONE_HANDLER = CommandHandler("phone", phone, run_async=True)

dispatcher.add_handler(PHONE_HANDLER)


__command_list__ = ["phone"]
__handlers__ = [PHONE_HANDLER]
