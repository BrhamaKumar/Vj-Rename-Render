# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20810825")

API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6693648608:AAE5ZMqOO9GtUzbUBDjWukV4YvyHoliiWYI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "demosaveforce") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://gitadevidevi053:Brhama025@cluster0.9rj57mi.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6301693754').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
