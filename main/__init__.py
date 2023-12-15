#Github.com/mrinvisible7

from pyrogram import Client, filters
from pyrogram.types import Message

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "28034111"
API_HASH = "3f89fab357b70e6556aa6a9e1d892b9d"
BOT_TOKEN = "6484894365:AAEagaHJ-zAP3i6SLlMNUleSBhGwKWduYOw"
SESSION = "BABbqRS2rE4g3fJ4C1tncdjoWeOCDWdHHSIvWY7cIFqvQLR15tAreFakxUS6KYP8FcNGh0Zne7W0CyJPAv_qBm1wUGuJXpojRYEQ4UIY52lQpUaST6lPwdIX-4Nz8x9rcbpVV3hIIiTS3Ln5Up604S-19am1uHv4BuC9bBqpWUVB4M8wCLWlosxFoeAWDvVnX_3xzjYnh5FmEgMIAwNj_GoY34fCtI8BSwrbiOJq7M0NUrEEOKQ1KmvfJWsluxB6gg7gHzluJJCW_1dqVpHd-qGDcXZ8tbzRAniD7qhRxSQE6VGTRNF9W4GT_NlDixcjOwJ5RZ9LF0_RevSws8IrkC1tAAAAAYSLfM0A"
FORCESUB = "dev_gagan"
AUTH = "6876018655"
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
