import codecs
import pickle
from asyncio import gather, get_running_loop
from io import BytesIO
from math import atan2, cos, radians, sin, sqrt
from random import randint
from re import findall
from time import time

import aiofiles
import aiohttp
import speedtest
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pyrogram.types import Message
from wget import download

from aries import aiohttpsession as aiosession
from aries import arq

from aries.utils.http import get

"""
Just import 'downloader' anywhere and do downloader.download() to
download file from a given url
"""
downloader = downloader.download()

# Another downloader, but with wget


async def download_url(url: str):
    loop = get_running_loop()
    file = await loop.run_in_executor(None, download, url)
    return file


def generate_captcha():
    # Generate one letter
    def gen_letter():
        return chr(randint(65, 90))

    def rndColor():
        return (randint(64, 255), randint(64, 255), randint(64, 255))

    def rndColor2():
        return (randint(32, 127), randint(32, 127), randint(32, 127))

    # Generate a 4 letter word
    def gen_wrong_answer():
        word = ""
        for _ in range(4):
            word += gen_letter()
        return word

    # Generate 8 wrong captcha answers
    wrong_answers = []
    for _ in range(8):
        wrong_answers.append(gen_wrong_answer())

    width = 80 * 4
    height = 100
    correct_answer = ""
    font = ImageFont.truetype("assets/arial.ttf", 55)
    file = f"assets/{randint(1000, 9999)}.jpg"
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw random points on image
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(4):
        letter = gen_letter()
        correct_answer += letter
        draw.text(
            (60 * t + 50, 15), letter, font=font, fill=rndColor2()
        )
    image = image.filter(ImageFilter.BLUR)
    image.save(file, "jpeg")
    return [file, correct_answer, wrong_answers]


def test_speedtest():
    def speed_convert(size):
        power = 2 ** 10
        zero = 0
        units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
        while size > power:
            size /= power
            zero += 1
        return f"{round(size, 2)} {units[zero]}"

    speed = speedtest.Speedtest()
    info = speed.get_best_server()
    download = speed.download()
    upload = speed.upload()
    return [speed_convert(download), speed_convert(upload), info]


async def file_size_from_url(url: str) -> int:
    async with aiosession.head(url) as resp:
        size = int(resp.headers["content-length"])
    return size


async def get_http_status_code(url: str) -> int:
    async with aiosession.head(url) as resp:
        return resp.status


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


async def transfer_sh(file_or_message):
    if is_instance(file_or_message, Message):
        file_or_message = await file_or_message.download()
    file = file_or_message
    async with aiofiles.open(file, "rb") as f:
        params = {file: await f.read()}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://transfer.sh/", data=params
        ) as resp:
            download_link = str(await resp.text()).strip()
    return download_link


def obj_to_str(object):
    if not object:
        return False
    string = codecs.encode(pickle.dumps(object), "base64").decode()
    return string


def str_to_obj(string: str):
    object = pickle.loads(codecs.decode(string.encode(), "base64"))
    return object


async def calc_distance_from_ip(ip1: str, ip2: str) -> float:
    Radius_Earth = 6371.0088
    data1, data2 = await gather(
        get(f"http://ipinfo.io/{ip1}"),
        get(f"http://ipinfo.io/{ip2}"),
    )
    lat1, lon1 = data1["loc"].split(",")
    lat2, lon2 = data2["loc"].split(",")
    lat1, lon1 = radians(float(lat1)), radians(float(lon1))
    lat2, lon2 = radians(float(lat2)), radians(float(lon2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        sin(dlat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = Radius_Earth * c
    return distance


def get_urls_from_text(text: str) -> bool:
    regex = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]
                [.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(
                \([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\
                ()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""".strip()
    return [x[0] for x in findall(regex, text)]


async def extract_userid(message, text: str):
    text = text.strip()
    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        # if reply to a message and no reason is given
        if not reply.from_user:
            return None, None
        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return reply.from_user.id, reason

    # if not reply to a message and no reason is given
    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None
    # if reason is given
    elif len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]


async def test_ARQ(message):
    results = ""
    funcs = {
        "deezer": arq.deezer("attention", 1),
        "image": arq.image("something"),
        "luna": arq.luna("hello"),
        "lyrics": arq.lyrics("attention"),
        "nlp": arq.nlp("bitcoin"),
        "nsfw_scan": arq.nsfw_scan(
            url="https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg"
        ),
        "pornhub": arq.pornhub("something"),
        "proxy": arq.proxy(),
        "pypi": arq.pypi("python-arq"),
        "reddit": arq.reddit("porn"),
        "quotly": arq.quotly(message),
        "saavn": arq.saavn("attention"),
        "stats": arq.stats(),
        "tmdb": arq.tmdb("flash"),
        "torrent": arq.torrent("porn"),
        "translate": arq.translate("hello"),
        "urbandict": arq.urbandict("wtf"),
        "wall": arq.wall("anime"),
        "wiki": arq.wiki("cat"),
        "youtube": arq.youtube("never gonna give you up"),
    }

    for key, value in funcs.items():
        try:
            t1 = time()
            result = await value
            t2 = time()
            if result.ok:
                results += f"**{key.capitalize()}:** `{t2-t1}`\n"
            else:
                resuls += f"**{key.capitalize()}:** `Failed`\n"
        except Exception:
            results += f"**{key.capitalize()}:** `Failed`\n"
    return results
