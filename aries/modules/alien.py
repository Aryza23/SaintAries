import cv2
from aries import tbot
from aries.events import register
import numpy as np
import math
from vcam import vcam,meshGen
import sys
import os
if not os.path.isdir("./dco/"):
    os.makedirs("./dco/")
from PIL import Image, ImageDraw
import pygments, os, asyncio, shutil, scapy, sys, requests, re, subprocess
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from telegraph import upload_file
from telethon import events
from telethon.tl.types import MessageMediaPhoto
import pygments, os, asyncio, shutil, scapy, sys, requests, re, subprocess, urllib
@register(pattern="^/alien")
async def fun_mirror(event):
    path = "dco"
    reply = await event.get_reply_message()
    lol = await tbot.download_media(reply.media, path)
    file_name = "mirror.jpg"
    hehe = path + "/" + file_name
    img = cv2.imread(lol)
    H,W = img.shape[:2]
    fps = 30
    c1 = vcam(H=H,W=W)
    plane = meshGen(H,W)
    plane.Z += 20*np.sin(2*np.pi*((plane.X-plane.W/4.0)/plane.W)) + 20*np.sin(2*np.pi*((plane.Y-plane.H/4.0)/plane.H))
    pts3d = plane.getPlane()
    pts2d = c1.project(pts3d)
    map_x,map_y = c1.getMaps(pts2d)
    output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR,borderMode=0)
    output = cv2.flip(output,1)
    out1 = cv2.resize(output,(700,350))
    cv2.imwrite(file_name,out1)
    await tbot.send_file(event.chat_id, file_name)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
    hoi = await event.delete()
client = tbot
path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)

@register(pattern="^/mirror")
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to media")
        return
    await event.reply("```Processing...```")
    reply = await event.get_reply_message()
    pathh = await tbot.download_media(reply.media, path)
    img = cv2.VideoCapture(pathh)
    iss,dan = img.read()
    ish = cv2.flip(dan, 1)
    misi = cv2.hconcat([dan, ish])
    cv2.imwrite('dark.jpg', misi)
    await event.client.send_file(event.chat_id, "dark.jpg" , reply_to=event.reply_to_msg_id) 
    await event.delete()
    shutil.rmtree(path)
    os.remove("dark.jpg")

@register(pattern="^/circle")
async def shiv(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any media.")
        return
    await event.reply("```Processing...```")
    reply = await event.get_reply_message()
    download = await tbot.download_media(reply.media, path)
    danish = cv2.VideoCapture(download) 
    ret, frame = danish.read()
    cv2.imwrite("danish.jpg", frame)
    img=Image.open("danish.jpg").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('shivam.webp')
    await event.client.send_file(event.chat_id, "shivam.webp", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("shivam.webp")
    os.remove("danish.jpg")
