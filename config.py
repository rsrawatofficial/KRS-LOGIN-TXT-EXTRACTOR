# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27900743"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "ebb06ea8d41420e60b29140dcee902fc")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7609528498:AAGqcl_h-Cygc4v_oiXqD4cbp-yGypVcakY")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@krstesting_bbottttbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7804396225"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7804396225").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002358701516"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://rsrasasingh:FS2G9YbI28KbPHLC@cluster0.yljr3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002358701516"))

