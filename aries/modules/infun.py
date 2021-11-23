#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# .tweet made for ultroid

# .uta ported from Dark-Cobra

"""
✘ Commands Available -

• `{i}uta <search query>`
    Inline song search and downloader.

• `{i}gglax <query>`
    Create google search sticker with text.

• `{i}stic <emoji>`
    Get random stickers from emoji.

• `{i}frog <text>`
    make text stickers.

• `{i}tweet <text>`
    make twitter posts.

• `{i}quot <text>`
    write quote on animated sticker.
"""

from random import choice

from telethon.errors import ChatSendInlineForbiddenError

from aries.utils.stickertools import deEmojify

from aries.events import register


@register(pattern="/tweet ?(.*)")
async def tweet(event):
    wai = await event.reply("`Processing...`")
    text = event.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await event.client.inline_query("twitterstatusbot", text)
        await event.reply("New Tweet", file=results[0].document)
        await wai.delete()
    except Exception as m:
        await event.reply(e, str(m))


@register(pattern="/stic ?(.*)")
async def tweet(event):
    if len(event.text) > 5 and event.text[5] != " ":
        return
    wai = await event.reply("`Processing...`")
    text = event.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Emoji !`")
    results = await event.client.inline_query("sticker", text)
    num = choice(results)
    await event.reply("@sticker", file=num.document)
    await wai.delete()


@register(pattern="/gglax ?(.*)")
async def gglax_sticker(event):
    wai = await event.reply("`Processing...`")
    text = event.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await event.client.inline_query("googlaxbot", text)
        await event.reply("Googlax", file=results[0].document)
        await wai.delete()
    except Exception as m:
        await event.reply(e, str(m))


@register(pattern="/frog ?(.*)")
async def honkasays(event):
    wai = await event.reply("`Processing...`")
    text = event.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give Me Some Text !`")
    text = deEmojify(text)
    if not text.endswith("."):
        text += "."
    if len(text) <= 9:
        q = 2
    elif len(text) >= 14:
        q = 0
    else:
        q = 1
    try:
        res = await event.client.inline_query("honka_says_bot", text)
        await event.reply("Honka", file=res[q].document)
        await wai.delete()
    except Exception as er:
        await wai.edit(str(er))


@register(pattern="/uta ?(.*)")
async def nope(event):
    ok = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    a = await event.reply("`Processing...`")
    if ok:
        pass
    elif replied and replied.message:
        ok = replied.message
    else:
        return await event.reply(
            "`Sir please give some query to search and download it for you..!`",
        )
    sticcers = await event.client.inline_query("Lybot", f"{(deEmojify(ok))}")
    await event.reply(file=sticcers[0].document)
    await a.delete()


@register(pattern="/quot ?(.*)")
async def quote_(event):
    IFUZI = event.pattern_match.group(1)
    if not IFUZI:
        return await event.reply("`Give some text to make Quote..`")
    EI_IR = await event.reply("`Processing...`")
    try:
        RE_ZK = await event.client.inline_query("@QuotAfBot", IFUZI)
        await event.reply(file=choice(RE_ZK).document)
    except Exception as U_TG:
        return await event.reply(EI_IR, str(U_TG))
    await EI_IR.delete()
