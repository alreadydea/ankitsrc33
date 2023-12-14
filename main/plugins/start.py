#Github.com/devgaganin

import os
from .. import bot as Invix
from telethon import events, Button
from io import BytesIO

#from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Invix.on(events.callbackquery.CallbackQuery(data="set"))
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
        
@Invix.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Invix = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  

@Invix.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "👋 Hi, I am 'Save Restricted Content Bot' Made with ❤️ __Gagan__\n\n✅ Send me the Link of any message of Restricted Channels to Clone it here..."

    photo_filename = 'photo.jpg'  # Replace with the actual filename of the photo

    try:
        with open(photo_filename, 'rb') as photo_file:
            photo_data = BytesIO(photo_file.read())

        await event.client.send_file(
            event.chat_id,
            file=photo_data,
            caption=text,
            buttons=[
                [Button.inline("SET THUMB.", data="set"),
                 Button.inline("REM THUMB.", data="rem")],
                Button.url("Join Channel", url="https://t.me/dev_gagan")
            ]
        )
    except FileNotFoundError:
        print(f"File not found: {photo_filename}")
    except Exception as e:
        print(f"Error: {e}")



    
    
