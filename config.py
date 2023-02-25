from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","cr bot")
BOT_USERNAME = getenv("BOT_USERNAME", "devfrawnbot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "devpokemon")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GRO_UP_1")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/b489a489ea1b536511c42.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/b489a489ea1b536511c42.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5190136458").split()))
