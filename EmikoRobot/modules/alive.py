import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/5323d00377327303737ff.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**𝙷𝙸 [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Emiko Robot.** \n\n"
  TEXT += "✮ **𝙸'𝙼 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈** \n\n"
  TEXT += f"✮ **𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 : [Idiot](https://t.me/SmartGoblok)** \n\n"
  TEXT += f"✮ **𝙻𝙸𝙱𝚁𝙰𝚁𝚈 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{telever}` \n\n"
  TEXT += f"✮ **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{tlhver}` \n\n"
  TEXT += f"✮ **𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{pyrover}` \n\n"
  TEXT += "**𝚃𝙷𝙰𝙽𝙺𝚂 𝙵𝙾𝚁 𝙰𝙳𝙳𝙸𝙽𝙶 𝙼𝙴 𝙷𝙴𝚁𝙴 😍**"
  BUTTON = [[Button.url("Help", "https://t.me/SmartGoblokbot?start=help"), Button.url("Support", "https://t.me/hayangeeh")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
