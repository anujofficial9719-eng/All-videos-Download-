import os
import time
import re

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # Pyrogram client config
    API_ID = os.environ.get("API_ID", "34724970")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "f240eae7c60e8e30c17203ab0e052f7e")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8799486461:AAH6td7_S68a3PnGNJermUgxA6_A1vhBS-c")  # ⚠️ Required
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Media_downloader_ak_bot")  # ⚠️ Required
    
    # Database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")  # ⚠️ Required
    
    # Other configs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/bjwFrTyy/7168219724-28773.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7892805795').split()]  # ⚠️ Required
    FORCE_SUB_TEXT = os.environ.get('FORCE_SUB_TEXT', "**You are not in our backup channel given below so you don't get the file...\n\nIf you want the file, click on the '❆ Join Our Backup Channel ❆' button below and join our backup channel, then click on the '↻ Try Again' button below...\n\nThen you will get the files...**")
    FORCE_SUB = os.environ.get('FORCE_SUB', 'save_content_ak_bot')  # ⚠️ Required
    AUTH_CHANNEL = -1001811608554  # Updated AUTH_CHANNEL value
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003515041061"))  # ⚠️ Required
    
    # Mega User Account ⚠️ Only Set When you have Pro or Enterprise Mega Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "ak14147800@gmail.com")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "thakur#12")
    
    # Web response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8081"))

class Txt(object):
    # Part of text configuration
    START_TXT = """<b>Hello {} 👋,
━━━━━━━━━━━━━━━━━━━━━
This Bot Can Search PornHub
Videos & Download Them For You

Can Also Download Files through
Link of Mega & YouTube
━━━━━━━━━━━━━━━━━━━━━
⚠️The Bot Contains 18+ Content
So Kindly Access it with Your own
Risk. Children Please Stay Away.
We don't intend to spread Pørno-
graphy here. It's just a bot for a
purpose as many of them wanted.
━━━━━━━━━━━━━━━━━━━━━
Click The Buttons Below To Search
"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 My name : {}
├👨‍💻 Programmer : <a href="https://t.me/anujedits76">Anuj Kumar</a>
├👑 Instagram : <a href="https://www.instagram.com/arafta_hindi_dubbed_hd">C-Insta</a>
├☃️ Founder of : <a href="https://t.me/anujedits76">ANUJ</a>
├📕 Library : <a href="https://github.com/pyrogram">Pyrogram</a>
├✏️ Language: <a href="https://www.python.org">Python 3</a>
├💾 Database: <a href="https://cloud.mongodb.com">Mongo DB</a>
├🌀 My Server : <a href="https://dashboard.heroku.com">Heroku</a>
╰───────────────⍟ """

    HELP_TXT = """
This Bot Will Help You To Download Following Files Through Links:

⊚ YouTube
⊚ Mega
⊚ PornHub

❗ Any Other Help Contact :- <a href="https://t.me/anujedits76">Support</a>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰Progress Bar❱━➣
┣⪼ 🗃️ Size: {1} | {2}
┣⪼ ⏳️ Done : {0}%
┣⪼ 🚀 Speed: {3}/s
┣⪼ ⏰️ ETA: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
