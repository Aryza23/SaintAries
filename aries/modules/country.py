import flag
from countryinfo import CountryInfo

from aries import telethn as borg
from aries.events import register


@register(pattern="^/country (.*)")
async def msg(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    lol = input_str
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await event.reply("Country Not Avaiable Currently")
    name = a.get("name")
    bb = a.get("altSpellings")
    hu = "".join(f'{p},  ' for p in bb)
    area = a.get("area")
    hell = a.get("borders")
    borders = "".join(f'{fk},  ' for fk in hell)
    WhAt = a.get("callingCodes")
    call = "".join(f'{what}  ' for what in WhAt)
    capital = a.get("capital")
    fker = a.get("currencies")
    currencies = "".join(f'{FKer},  ' for FKer in fker)
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iso = ""
    iSo = a.get("ISO")
    for hitler in iSo:
        po = iSo.get(hitler)
        iso += f'{po},  '
    fla = iSo.get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)

    languages = a.get("languages")
    lMAO = "".join(f'{lmao},  ' for lmao in languages)
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tik = a.get("timezones")
    tom = "".join(f'{jerry},   ' for jerry in tik)
    GOT = a.get("tld")
    lanester = "".join(f'{targaryen},   ' for targaryen in GOT)
    wiki = a.get("wiki")

    caption = f"""<b><u>Information Gathered Successfully</b></u>
<b>
Country Name:- {name}
Alternative Spellings:- {hu}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's Capital:- {capital}
Country's currency:- {currencies}
Country's Flag:- {okie}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Languages:- {lMAO}
Native Name:- {nonive}
population:- {waste}
Region:- {reg}
Sub Region:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}
wikipedia:- {wiki}</b>

Gathered By Aries.</b>
"""

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )


__mod_name__ = "country"
