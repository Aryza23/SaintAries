import os
import psutil
from pySmartDL import SmartDL
from aries import pbot
from aries import DRAGONS as sudo_users
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup

def progress(current, total):
        print(f"{current * 100 / total:.1f}%") 


@pbot.on_message(filters.command(["dl"]))
async def download (client , message):
    try:
        await message.reply_text(text = f"**Got link.. Downloading 🥺")
        url = message.reply_to_message.text
        desti = './cache/'

        disable_web_page_preview = True
        chat_id = message.chat.id
        obj = SmartDL(url, desti)
        obj.start()
        filename = path = obj.get_dest()
        await pbot.send_document(chat_id ,filename , caption="uploaded by Aries" , progress=progress )
        await message.reply_text(text = f"**Uploaded Successfully! 🥺")
        os.remove(filename) 
    except:
        await message.reply_text(text = "ERROR OCCURED PLS DONT CONTACT @RAVEEN2003")

@pbot.on_message(filters.command(["statsdl"], prefixes = ["." ]))
async def stats (client , message):
    user_id = message.from_user.id
    if user_id in sudo_users:
        chat_id = message.chat.id
        print(os.uname()) 
        os_unmae = str( os.uname())
        disk_stat =  str(psutil.disk_usage('/'))
        print(psutil.disk_usage('/'))
        status = str( "RUNNING IN HEROKU , WANNA DOANTE VPS ? check /donate")
        await message.reply_text(text = "**\n\nHOSTNAME:** " +os_unmae + " "+ " "  + " "+ " "+ "\n\n **STORAGE**:" + disk_stat +  " " + " " +" " + " "+"\n\n **RUNNING STATUS :**" + status )
    else:
        await message.reply_text(text= "you are not a sudo user of Aries")
        await message.reply_text(text = "Hosted on heroku , /donate for more speed!")

@pbot.on_message(filters.command(["aboutdl"], prefixes = ["." , "wtf_"]))
async def about (client , message):
    keyboard = [
        [
            InlineKeyboardButton("support",
                                          url="https://t.me/idzeroidsupport"),
            InlineKeyboardButton("update",url="https://t.me/idzeroid")
        ],
    ]
    await message.reply_text(text =
                              "<b>Hey! My name is Aries.</b>"
                              "\nI can Download and Upload Files for You senpai."
                              "\n\n<b>About Me :</b>"
                              "\n\n  - <b>Name</b>        : <a href=\"https://t.me/idzeroid_bot/\">Aries</a>"
                              "\n\n  - <b>Creator</b>      : <a href=\"https://t.me/idzxartez/\">Aryza</a>"
                              "\n\n  - <b>Language</b>  : <a href=\"https://www.python.org/\">Python 3</a>"
                              "\n\n  - <b>Library</b>       : <a href=\"https://docs.pyrogram.org//\">PYROGRAM</a>"
                              "\n\n  - <b>Github Page</b>  : <a href=\"https://github.com/idzero23\">Idzeroid</a>",    
        disable_web_page_preview = True ,
        reply_markup = InlineKeyboardMarkup(keyboard)
     )


@pbot.on_message(filters.command(["helpdl"]))
async def help (client , message):
    await message.reply_text(text = "<b> Need help ? </b>"
                                    "<b> \n\n I can help you download files less than 2GB </b>"
                                    "<b> \n\n Just send me a link and reply it with /dl </b>"
                                    "<b> \n\n To know More About me &  to get Source Code /about </b>"
                                    "<b> \n\n /support to get support </b>"
                                    "<b> \n\n /donate to donate this bot !</b>")

@pbot.on_message(filters.command(["support"]))
async def support(client , message):
    await message.reply_text(text = "<b> currently there is no support for this bot🥺! </b>"
                                    "<b> \n\n JOIN @idzeroidsupport !</b>"
                                    "<b>\n\n Update bot @idzeroid")


@pbot.on_message(filters.command(["donateme"]))
async def donate(client , message):
    keyboard = [
        [
            InlineKeyboardButton("github",
                                          url="https://github.com/idzero23"),
            InlineKeyboardButton("Owner",url="https://t.me/idzxartez"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text("Thank you for comming forwad to donate" , reply_markup=reply_markup)


