
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


from pyrogram import Client, Filters, MessageHandler, CallbackQueryHandler
from robot.commands import *
logging.getLogger("pyrogram").setLevel(logging.WARNING)



if __name__ == "__main__" :
        #Lets create our download directory, if it doesnt exist
        if not os.path.isdir("./DOWNLOADS"):
            os.makedirs("./DOWNLOADS")
            token_bot = "852481793:AAGLxh1MyAXOZoRivts7wtEt7ay1ejQYDi4"
            bot = Client("my_bot",
                         bot_token=token_bot,
                         api_id=API_ID,
                         api_hash="API_HASH",
                         workers=100
            )
            bot.DOWNLOAD_WORKERS = 100
	    #Lets create commands for our bot
            bot.add_handler(MessageHandler(startBot, filters=Filters.command(["start"], prefixes=["/", "!", "$", "#"])))      
            bot.add_handler(MessageHandler(help_func, 
	    filters=Filters.command(["help"], prefixes=["/", "!", "$", "#"]))
	    )
            bot.add_handler(MessageHandler(
                rename_func, 
	        filters=Filters.command(["rename"], prefixes=["/"]))
	    )
            bot.add_handler(MessageHandler(upload_func, 
	    filters=Filters.command(["upload"], prefixes=["/"]))
	    )
            bot.add_handler(MessageHandler(
                savethumbnail_func, 
	        filters=Filters.command(["savethumbnail"], prefixes=["/"]))
	    ) 
        bot.run()
	
