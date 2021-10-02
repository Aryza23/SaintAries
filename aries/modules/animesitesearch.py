import html

import bs4
import requests
from aries import dispatcher
from aries.modules.disable import DisableAbleCommandHandler
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.ext import CallbackContext, run_async

info_btn = "More Information"
kayo_btn = "Kayo 🏴‍☠️"
animespot_btn = "Animespot ☠️"
animetm_btn = "Animetm ☠️"
prequel_btn = "⬅️ Prequel"
sequel_btn = "Sequel ➡️"
close_btn = "Close ❌"


def site_search(update: Update, context: CallbackContext, site: str):
    message = update.effective_message
    args = message.text.strip().split(" ", 1)
    more_results = True

    try:
        search_query = args[1]
    except IndexError:
        message.reply_text("Give something to search")
        return

    if site == "kayo":
        search_url = f"https://animekayo.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"
            
    elif site == "animespot":
        search_url = f"https://dubspotteam.blogspot.com/?q={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Animespotdubber</code>: \n"
        for entry in search_result:
                 
           if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeSpot</code>"
                more_results = False
                break
                
           post_link = entry.a['href']
           post_name = html.escape(entry.text.strip())
           result += f"• <a href='{post_link}'>{post_name}</a>\n"
           
    elif site == "animetm":
        search_url = f"https://animetmdubbers.in/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"}) 
        
        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Animetmdubber</code>: \n"
        for entry in search_result:
                 
           if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>"
                more_results = False
                break
                
           post_link = entry.a['href']
           post_name = html.escape(entry.text.strip())
           result += f"• <a href='{post_link}'>{post_name}</a>\n"
           
    buttons = [[InlineKeyboardButton("See all results", url=search_url)]]

    if more_results:
        message.reply_text(
            result,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)
    else:
        message.reply_text(
            result, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@run_async
def kayo(update: Update, context: CallbackContext):
    site_search(update, context, "kayo")
    
@run_async
def animespot(update: Update, context: CallbackContext):
    site_search(update, context, "animespot")
   
@run_async
def animetm(update: Update, context: CallbackContext):
    site_search(update, context, "animetm")


__help__ = """
• `/animetm`*:* Find anime from animetm dubbers website.
• `/animespot`*:* Find anime from animespot website.
• `/kayo`*:* Find anime from animekayo website.
"""
    
__mod_name__ = "Anime Site Search"
KAYO_SEARCH_HANDLER = DisableAbleCommandHandler("kayo", kayo)
ANIMESPOT_SEARCH_HANDLER = DisableAbleCommandHandler("animespot", animespot)
ANIMETM_SEARCH_HANDLER = DisableAbleCommandHandler("animetm", animetm)

dispatcher.add_handler(KAYO_SEARCH_HANDLER)
dispatcher.add_handler(ANIMESPOT_SEARCH_HANDLER)
dispatcher.add_handler(ANIMETM_SEARCH_HANDLER)

__handlers__ = [ KAYO_SEARCH_HANDLER,
     ANIMESPOT_SEARCH_HANDLER,  ANIMETM_SEARCH_HANDLER]
