from hitsuki.modules.sql.translation import prev_locale
from hitsuki.modules.translations.English import EnglishStrings
from hitsuki.modules.translations.Indonesian import IndonesianStrings


def tld(chat_id, t, show_none=True):
    LANGUAGE = prev_locale(chat_id)
    print(chat_id, t)
    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('pt') and t in IndonesianStrings:
            return IndonesianStrings[t]
        else:
            if t in EnglishStrings:
                return EnglishStrings[t]
            else:
                return t
    elif show_none:
        if t in EnglishStrings:
            return EnglishStrings[t]
        else:
            return t


def tld_help(chat_id, t):
    LANGUAGE = prev_locale(chat_id)
    print("tld_help ", chat_id, t)
    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name

        t = t + "_help"

        print("Test2", t)

        if LOCALE in ('pt') and t in IndonesianStrings:
            return IndonesianStrings[t]
        else:
            return False
    else:
        return False
