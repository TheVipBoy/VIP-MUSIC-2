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
API_HASH = getenv("API_HASH", "13a970c9a89de170ee3382fea86eb4cf")
API_ID = int(getenv("API_ID", "14334990"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "MISS_RIYA_JI")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/cfcad824b691f3c9a5c0e.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "5617790188:AAHrBAsBii1wsN4f__FYuStfo7y9Arki1QI")
BOT_USERNAME = getenv("BOT_USERNAME", "TG_MANAGER_ROBOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "STD KING")
OWNER_USERNAME = getenv("OWNER_USERNAME", "THE_VIP_BOY")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/Team_STD_Network")
STRING_SESSION = getenv("STRING_SESSION", "AgBSUudwi_JQVmlbEvYbrsBUHiY-8Dqoq_83xQOOopsQrjzAx4kQPyUB97saq9w6lvGfEeK3Z5aUx-Hy2oc5PfkWiLnXyVzcfSo_qDmHlc4EQX0B0fd_xE-GTcGe5lFC5t0cyq6U02sRY_J9RLsGHysHfS9KECJKruz83daNz3C5sJxMJ6RohtrqS6DDpYnNwoTbwdeUZyVUgEQh7a2KDiGIXb_FAiSl3rXEhYz_YR26NvjwIPvZFQdkuRDx9_XInM7mDDKh_QfFJjSLwy20hXM8-U8Z4_GCaA3oBpOhMu5euoLra312dkSELoTJlK8NQkQKnZAyoMCqIcB6kgAI9fV9AAAAATNrKYMA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5157628291").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Mahakal_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/Mahakal_update")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/Team_STD_Network")
