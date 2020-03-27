import os

class Config (object):
        #The Download Location from our bot server
        download_location = "./DOWNLOADS"
        # get a token from @BotFather
        TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
        # The Telegram API things
        APP_ID = int(os.environ.get("APP_ID", 12345))
        API_HASH = os.environ.get("API_HASH")
        # Telegram maximum file upload size
        MAX_FILE_SIZE = 50000000
        TG_MAX_FILE_SIZE = 1572864000
        FREE_USER_MAX_FILE_SIZE = 50000000
        # chunk size that should be used with requests
        CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
        # maximum message length in Telegram
        MAX_MESSAGE_LENGTH = 4096
