import asyncio
import os
import re
import better_profanity
import emoji
import nude
import requests

from better_profanity import profanity
from google_trans_new import google_translator
from telethon import events
from telethon.tl.types import ChatBannedRights
from pymongo import MongoClient

from aries.pyrogramee.telethonbasics import is_admin
from aries.events import register
from aries.modules.sql.nsfw_watch_sql import (
    add_nsfwatch,
    get_all_nsfw_enabled_chat,
    is_nsfwatch_indb,
    rmnsfwatch,
)
from aries import telethn as tbot
from aries import MONGO_DB_URI

translator = google_translator()
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["aries"]


async def is_nsfw(event):
    lmao = event
    if not (
        lmao.gif
        or lmao.video
        or lmao.video_note
        or lmao.photo
        or lmao.sticker
        or lmao.media
    ):
        return False
    if lmao.video or lmao.video_note or lmao.sticker or lmao.gif:
        try:
            starkstark = await event.client.download_media(lmao.media, thumb=-1)
        except:
            return False
    elif lmao.photo:
        try:
            starkstark = await event.client.download_media(lmao.media)
        except:
            return False
    img = starkstark
    f = {"file": (img, open(img, "rb"))}

    r = requests.post("https://starkapi.herokuapp.com/nsfw/", files=f).json()
    if r.get("success") is False:
        is_nsfw = False
    elif r.get("is_nsfw") is True:
        is_nsfw = True
    elif r.get("is_nsfw") is False:
        is_nsfw = False
    return is_nsfw


@tbot.on(events.NewMessage(pattern="/gshield (.*)"))
async def nsfw_watch(event):
    if not event.is_group:
        await event.reply("You Can Only Nsfw Watch in Groups.")
        return
    input_str = event.pattern_match.group(1)
    if not await is_admin(event, 1192108540):
        await event.reply("`I Should Be Admin To Do This!`")
        return
    if await is_admin(event, event.message.sender_id):
        if input_str in ["on", "On", "ON", "enable"]:
            if is_nsfwatch_indb(str(event.chat_id)):
                await event.reply("`This Chat Has Already Enabled Nsfw Watch.`")
                return
            add_nsfwatch(str(event.chat_id))
            await event.reply(
                f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Groups Nsfw Contents Will Be Deleted**"
            )
        elif input_str in ["off", "Off", "OFF", "disable"]:
            if not is_nsfwatch_indb(str(event.chat_id)):
                await event.reply("This Chat Has Not Enabled Nsfw Watch.")
                return
            rmnsfwatch(str(event.chat_id))
            await event.reply(
                f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Nsfw Watch**"
            )
        else:
            await event.reply(
                "I undestand `/nsfwguardian on` and `/nsfwguardian off` only"
            )
    else:
        await event.reply("`You Should Be Admin To Do This!`")
        return


@tbot.on(events.NewMessage())
async def ws(event):
    warner_starkz = get_all_nsfw_enabled_chat()
    if len(warner_starkz) == 0:
        return
    if not is_nsfwatch_indb(str(event.chat_id)):
        return
    if not (event.photo):
        return
    if not await is_admin(event, 1192108540):
        return
    if await is_admin(event, event.message.sender_id):
        return
    sender = await event.get_sender()
    await event.client.download_media(event.photo, "nudes.jpg")
    if nude.is_nude("./nudes.jpg"):
        await event.delete()
        st = sender.first_name
        hh = sender.id
        final = f"**NSFW DETECTED**\n\n{st}](tg://user?id={hh}) your message contain NSFW content.. So, Aries deleted the message\n\n **Nsfw Sender - User / Bot :** {st}](tg://user?id={hh})  \n\n`⚔️Automatic Detections Powered By Aries` \n**#GROUP_GUARDIAN** "
        dev = await event.respond(final)
        await asyncio.sleep(30)
        await dev.delete()
        os.remove("nudes.jpg")


approved_users = db.approve
spammers = db.spammer
globalchat = db.globchat

CMD_STARTERS = "/"
profanity.load_censor_words_from_file("./profanity_wordlist.txt")


@register(pattern="^/profanity(?: |$)(.*)")
async def profanity(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.reply("You Can Only profanity in Groups.")
        return
    event.pattern_match.group(1)
    if not await is_admin(event, 1192108540):
        await event.reply("`I Should Be Admin To Do This!`")
        return
    if await is_admin(event, event.message.sender_id):
        input = event.pattern_match.group(1)
        chats = spammers.find({})
        if not input:
            for c in chats:
                if event.chat_id == c["id"]:
                    await event.reply(
                        "Please provide some input yes or no.\n\nCurrent setting is : **on**"
                    )
                    return
            await event.reply(
                "Please provide some input yes or no.\n\nCurrent setting is : **off**"
            )
            return
        if input == "on" and event.is_group:
            chats = spammers.find({})
            for c in chats:
                if event.chat_id == c["id"]:
                    await event.reply(
                        "Profanity filter is already activated for this chat."
                    )
                    return
            spammers.insert_one({"id": event.chat_id})
            await event.reply("Profanity filter turned on for this chat.")
        if input == "off":
            if event.is_group:
                chats = spammers.find({})
                for c in chats:
                    if event.chat_id == c["id"]:
                        spammers.delete_one({"id": event.chat_id})
                        await event.reply("Profanity filter turned off for this chat.")
                        return
            await event.reply("Profanity filter isn't turned on for this chat.")
        if input not in ["on", "off"]:
            await event.reply("I only understand by on or off")
            return
    else:
        await event.reply("`You Should Be Admin To Do This!`")
        return


@register(pattern="^/globalmode(?: |$)(.*)")
async def profanity(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await event.reply("You Can Only enable global mode Watch in Groups.")
        return
    event.pattern_match.group(1)
    if not await is_admin(event, 1192108540):
        await event.reply("`I Should Be Admin To Do This!`")
        return
    if await is_admin(event, event.message.sender_id):

        input = event.pattern_match.group(1)
        chats = globalchat.find({})
        if not input:
            for c in chats:
                if event.chat_id == c["id"]:
                    await event.reply(
                        "Please provide some input yes or no.\n\nCurrent setting is : **on**"
                    )
                    return
            await event.reply(
                "Please provide some input yes or no.\n\nCurrent setting is : **off**"
            )
            return
        if input == "on" and event.is_group:
            chats = globalchat.find({})
            for c in chats:
                if event.chat_id == c["id"]:
                    await event.reply(
                        "Global mode is already activated for this chat."
                    )
                    return
            globalchat.insert_one({"id": event.chat_id})
            await event.reply("Global mode turned on for this chat.")
        if input == "off":
            if event.is_group:
                chats = globalchat.find({})
                for c in chats:
                    if event.chat_id == c["id"]:
                        globalchat.delete_one({"id": event.chat_id})
                        await event.reply("Global mode turned off for this chat.")
                        return
            await event.reply("Global mode isn't turned on for this chat.")
        if input not in ["on", "off"]:
            await event.reply("I only understand by on or off")
            return
    else:
        await event.reply("`You Should Be Admin To Do This!`")
        return


@tbot.on(events.NewMessage(pattern=None))
async def del_profanity(event):
    if event.is_private:
        return
    msg = str(event.text)
    sender = await event.get_sender()
    # let = sender.username
    if await is_admin(event, event.message.sender_id):
        return
    chats = spammers.find({})
    for c in chats:
        if (
            event.text
            and event.chat_id == c["id"]
            and better_profanity.profanity.contains_profanity(msg)
        ):
            await event.delete()
            if sender.username is None:
                st = sender.first_name
                hh = sender.id
                final = f"[{st}](tg://user?id={hh}) **{msg}** is detected as a slang word and your message has been deleted"
            else:
                final = f"Sir **{msg}** is detected as a slang word and your message has been deleted"
            dev = await event.respond(final)
            await asyncio.sleep(10)
            await dev.delete()
        if event.photo and event.chat_id == c["id"]:
            await event.client.download_media(event.photo, "nudes.jpg")
            if nude.is_nude("./nudes.jpg"):
                await event.delete()
                st = sender.first_name
                hh = sender.id
                final = f"**NSFW DETECTED**\n\n{st}](tg://user?id={hh}) your message contain NSFW content.. So, Daisy deleted the message\n\n **Nsfw Sender - User / Bot :** {st}](tg://user?id={hh})  \n\n`⚔️Automatic Detections Powered By Aries Robot` \n**#GROUP_GUARDIAN** "
                dev = await event.respond(final)
                await asyncio.sleep(10)
                await dev.delete()
                os.remove("nudes.jpg")


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


@tbot.on(events.NewMessage(pattern=None))
async def del_profanity(event):
    if event.is_private:
        return
    msg = str(event.text)
    sender = await event.get_sender()
    # sender.username
    if await is_admin(event, event.message.sender_id):
        return
    chats = globalchat.find({})
    for c in chats:
        if event.text and event.chat_id == c["id"]:
            u = msg.split()
            emj = extract_emojis(msg)
            msg = msg.replace(emj, "")
            if (
                [(k) for k in u if k.startswith("@")]
                and [(k) for k in u if k.startswith("#")]
                and [(k) for k in u if k.startswith("/")]
                and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []
            ):
                h = " ".join(filter(lambda x: x[0] != "@", u))
                km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
                tm = km.split()
                jm = " ".join(filter(lambda x: x[0] != "#", tm))
                hm = jm.split()
                rm = " ".join(filter(lambda x: x[0] != "/", hm))
            elif [(k) for k in u if k.startswith("@")]:
                rm = " ".join(filter(lambda x: x[0] != "@", u))
            elif [(k) for k in u if k.startswith("#")]:
                rm = " ".join(filter(lambda x: x[0] != "#", u))
            elif [(k) for k in u if k.startswith("/")]:
                rm = " ".join(filter(lambda x: x[0] != "/", u))
            elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
                rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
            else:
                rm = msg
            # print (rm)
            b = translator.detect(rm)
            if "en" not in b and b != "":
                await event.delete()
                st = sender.first_name
                hh = sender.id
                final = f"[{st}](tg://user?id={hh}) you should only speak in english here !"
                dev = await event.respond(final)
                await asyncio.sleep(10)
                await dev.delete()


#

__help__ = """
Aries can protect your group from NSFW senders, Slag word users and also can force members to use English

🔘 *Commmands*:
  ❍ `/gshield <on/off>`*:* Enable|Disable Porn cleaning
  ❍ `/globalmode <on/off>`*:* Enable|Disable English only mode
  ❍ `/profanity <on/off>`*:* Enable|Disable slag word cleaning
"""
__mod_name__ = "Shield"
