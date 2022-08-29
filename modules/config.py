# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "")
API_ID = int(getenv("API_ID", ""))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GOOGLE MUSIC PLAYER")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Shizuka_X_Bot")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/94a4b839ca24c1c4d34f3.jpg")
BOT_NAME = getenv("BOT_NAME", "MUSIC PLAYER")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_USERNAME = getenv("BOT_USERNAME", "Google_Music2_RoBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
OWNER_NAME = getenv("OWNER_NAME", "[𝗔𝗙𝗞] ➫➬ 𝘾𝙪𝙩𝙚𝙗𝙤𝙮 ✘🇩™」[❤️]")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Error_17_4")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/VIP_DUNIA")
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1808943146 5380004155 5375901665").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/VIP_DUNIA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/VIP_CREATORS")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/VIP_CREATORS")
