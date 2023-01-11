from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID",
"17053751")
APP_HASH = os.environ.get("APP_HASH",
"6f90a1382848f5cc767a623f898ab23f")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
