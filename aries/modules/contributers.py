import github
from pyrogram import filters
from aries import pbot as app
from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters


IDZ = "https://telegra.ph/file/08f41dc969408c08b8c68.jpg"


@app.on_message(filters.command("repo") & ~filters.edited)
async def give_repo(c, m):
    g = github.Github()
    list_of_users = ""
    count = 0
    repo = g.get_repo("idzero23/SaintAries")
    for i in repo.get_contributors():
        count += 1
        list_of_users += f"•{count}. [{i.login}](https://github.com/{i.login})\n"
    await m.reply_photo(
        photo=IDZ,
        caption=f"""**Hey I'm Aries Robot** 
**Owner repo : [Aryza](https://t.me/idzxartez)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`

```----------------
| Collaborators |
----------------```
{list_of_users}
**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://github.com/idzero23/SaintAries"
                    ),
                ],
                [
                    InlineKeyboardButton("Support", url="https://t.me/idzeroidsupport"),
                    InlineKeyboardButton("Update", url="https://t.me/idzeroid"),
                ],
            ]
        ),
    )


__mod_name__ = "REPO"
