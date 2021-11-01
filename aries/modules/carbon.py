from pyrogram import filters

from aries import pbot
from aries.function.carbonfunc import make_carbon
from aries.utils.errors import capture_err


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_document(message.chat.id, carbon)
    await m.delete()
    carbon.close()


__help__ = """
❍ `/carbon` <text> [or reply]
  
Usage: Beautify your code using carbon.now.sh
"""

__mod_name__ = "🔘 Carbon"
