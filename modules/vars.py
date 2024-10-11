import os

API_ID    = os.environ.get("API_ID", "23701738")
API_HASH  = os.environ.get("API_HASH", "28f54cde54548df7354035c038ab3ddd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7130342243:AAHGQ0sTu9SLiJJ58Q7XD5B0v4RF88pZfAI") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
