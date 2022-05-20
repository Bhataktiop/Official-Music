import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc7ba397bb66523469e62.jpg",
        caption=f"""**⛦➪ Ꮋᴇʟʟᴏ Ꮖ ᴀᴍ  Տᴜᴘᴇʀ ҒᴀՏᴛ  ᎷᴜՏɪᴄ Ꮲʟᴀʏᴇʀ Ꮯʀᴇᴀᴛᴇᴅ Ᏼʏ [𝐌𝐑 𝐄𝐗𝐈𝐓](http//t.me/GIRLS_CRUSH_OUT_OF_RANGE)
⛦➪ Ᏼᴏᴛ Ғᴏʀ Ͳᴇʟᴇɢʀᴀᴍ ᏀʀᴏᴜᴘՏ...""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᗩᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Ꮐʀᴏᴜᴘ ➕",
                        url=f"https://t.me/SMEXY_xDBOT?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📨 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/A_BUT/32"
                    ),
                    InlineKeyboardButton(
                        "ՄᴘᴅᴀᴛᴇՏ 📢", url=f"https://t.me/A_BUT"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🚑 Ꮯʜᴀᴛ Ꮓᴏɴᴇ 🕊️", url=f"https://t.me/BHATAKTI_SUPPORTS")
                ]
                
           ]
        ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bc7ba397bb66523469e62.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒️ Source Code ⚒️", url=f"https://t.me/A_BUT/32")
                ]
            ]
        ),
    )
