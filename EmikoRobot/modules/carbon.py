from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from EmikoRobot import pbot
from EmikoRobot.utils.errors import capture_err
from EmikoRobot.utils.functions import make_carbon


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
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/5323d00377327303737ff.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **𝙷𝙴𝚈 𝙸'𝙼 𝙴𝙼𝙸𝙺𝙾 𝚁𝙾𝙱𝙾𝚃** 

**𝙾𝚆𝙽𝙴𝚁 𝚁𝙴𝙿𝙾 : [Raisa](https://t.me/RaisaAkemi)**
**𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{y()}`
**𝙻𝙸𝙱𝚁𝙰𝚁𝚈 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{o}`
**𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{s}`
**𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `{z}`

**𝙲𝚁𝙴𝙰𝚃𝙴 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝚆𝙸𝚃𝙷 𝙲𝙻𝙸𝙲𝙺 𝙱𝚄𝚃𝚃𝙾𝙽 𝙱𝙴𝙻𝙻𝙾𝚆.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url="https://github.com/kennedy-ex/emikorobot"), 
                    InlineKeyboardButton(
                        "Support", url="https://t.me/kememlupink")
                ]
            ]
        )
    )
