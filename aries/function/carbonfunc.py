from io import BytesIO

from aries import aiohttpsession as aiosession


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "Aries_carbon.png"
    return image
