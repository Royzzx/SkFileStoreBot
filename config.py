#(©)Rapid_Bots

import os
import logging
from script import ADMINS
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "15912260"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5c7ba9544c4d7cf3fecefebf1fd6f8bc")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002050257310"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "533890503"))

#Port
PORT = os.environ.get("PORT", "8080")

#fast dl link if need set True else set false (must use capital T)
STREAM = os.environ.get("STREAM", "True")

#Auto delete feature if need set True else set false (must use capital T)
DELETE = os.environ.get("DELETE", "false")

#start msg without verify if need set True else set false (must use capital T)
SRT_VERIFY = os.environ.get("SRT_VERIFY", "false")

#verify URL if need set True else set false (must use capital T)
VERIFY = os.environ.get("VERIFY", "false")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://MovieFive:8056939684@cluster0.0ovdo8e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = lambda: int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = lambda: True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(533890503)

LOG_FILE_NAME = "filesharingbot.txt"

FL_CHANNEL = int(os.environ.get("FL_CHANNEL", "-1002050257310"))

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
