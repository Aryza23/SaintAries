from aiohttp import ClientSession
from Python_ARQ import ARQ

from aries import ARQ_API_KEY

ARQ_API_URL = "https://grambuilders.tech"

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
