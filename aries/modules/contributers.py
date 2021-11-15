import github
from pyrogram import filters
from aries import pbot as app


@app.on_message(filters.command("repo") & ~filters.edited)
async def give_repo(c, m):
    g = github.Github()
    list_of_users = ""
    count = 0
    repo = g.get_repo("idzero23/SaintAries")
    for i in repo.get_contributors():
        count += 1
        list_of_users += f"*{count}.* [{i.login}](https://github.com/{i.login})\n"
    text = f"""[Github](https://github.com/idzero23/SaintAries) | [support group](https://t.me/idzeroidsupport)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await m.reply(text, disable_web_page_preview=False)


__mod_name__ = "REPO"
