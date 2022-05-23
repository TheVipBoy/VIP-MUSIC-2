import re
import os
import aiohttp
import asyncio
import logging
import requests
from os import getenv
from pyrogram.types import *
from datetime import datetime
from dotenv import load_dotenv
from pyrogram import Client, filters, idle
from apscheduler.schedulers.asyncio import AsyncIOScheduler


if os.path.exists("local.env"):
    load_dotenv("local.env")
    
    
# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
que = {}
admins = {}
CMD_HELP = {}
START_TIME = datetime.now()
scheduler = AsyncIOScheduler()
aiohttpsession = aiohttp.ClientSession()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
API_ID = int(getenv("API_ID", "12380656"))
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/1d6f55f754c0ad3b69048.jpg")
DATABASE_URL = getenv("DATABASE_URL", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
LOGS_GROUP_ID = getenv("LOGS_GROUP_ID", "")
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5356564375").split()))

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

if LOGS_GROUP_ID:
    Owner = LOGS_GROUP_ID
else:
    Owner = 777000
