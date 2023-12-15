#Github.com/mrinvisible7

import os
from .. import bot as Invix
from telethon import events, Button
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


S = "/start"
START_PIC = "https://graph.org/file/ffd7da274e555ed3a9fee.jpg"
TEXT = "👋 Hi, I am 'Save Restricted Content' bot Made with ❤️ by __**Team SPY**__\n\n✅ Send me the Link of any message of Restricted Channels to Clone it here.\nFor private channel's messages, send the Invite Link first.\n\n👨🏻‍💻Owner: https://telegram.dog/Mister_invisiblebot.\n**support:** https://telegram.dog/mr_invisible_bots"

@Invix.on_callback_query(filters.regex("^set$"))
async def sett(event):    
    Invix = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Invix.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@Invix.on_callback_query(filters.regex("^rem$"))
async def remt(event):  
    Invix = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        

@Invix.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    # Creating inline keyboard with buttons
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("SET THUMB.", callback_data="set"),
         InlineKeyboardButton("REM THUMB.", callback_data="rem")],
        [InlineKeyboardButton("Join Channel", url="https://telegram.dog/dev_gagan")]
    ])

    # Sending message with photo, caption, and buttons
    await message.reply_photo(
        START_PIC,
        caption=TEXT,
        reply_markup=reply_markup
    )
