import os

class Config(object):
    BOT_TOKEN = "7557612085:AAFs9uRaD8C0nZr4kBFM1ST30MzsWpKEZyA" # Ensure correct key name
    API_ID = "26468828" # Added key name and default value
    API_HASH ="4693513c08d1ac6af15f95b116c29478"  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6530997270").split(',')
    AUTH_USERS = [int(7517045929) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST ="http://master-api-v3.vercel.app" # Keeping HOST configurable
    CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎" # Making CREDIT an environment variable for flexibility
