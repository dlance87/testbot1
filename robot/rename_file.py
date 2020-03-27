
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import os
import time
from pyrogram import Client

from robot.commands import rename_func

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

thumb_image_path = Config.download_location + "/thumb_image.jpg"

#Lets first download our file into our bot server
async def rename_file(bot, update):
    await asyncio.sleep(1)
    chat_id = message.chat.id
    
    if message.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path

    if not os.path.isdir(Config.download_location):
        os.makedirs(Config.download_location)
        
        
        a = await bot.send_message(
                text=Translation.RENAMING_FILE ,
                chat_id=update.chat.id,
                message_id=update.message_id
        )
        b = await bot.edit_message_text(
                text="..patience,trying to download ",
                chat_id=update.chat.id,
                message_id=update.message_id
        )
        start = datetime.now()
        
        to_download_directory = Config.download_location
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        c_time = time.time()

        
        downloaded_file_name = await bot.download_media(
            message = update.reply_to_message,
            file_name = downloaded_file_name,
            progress_args=(
                Translation.DOWNLOAD_START,
                a,
                c_time
            )
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        new_file_name = to_download_directory + file_name
        os.rename(downloaded_file_name, new_file_name)
        

        if os.path.exists(new_file_name):
            c_time = time.time()
            await bot.send_document(
                message_id=a.message_id,
                chat_id=update.chat.id,
                document=new_file_name,
                thumb=thumb,
                supports_streaming=False,
                allow_cache=False,
                progress_args=(
                    Translation.UPLOAD_START,
                    a, 
                    c_time
                )
            )
            end_two = datetime.now()
            os.remove(new_file_name)
            ms_two = (end_two - end).seconds
            await bot.edit_message_text("Downloaded in {} seconds & Uploaded Successfully in {} seconds.".format(ms_one, ms_two))
            
        else:
             await bot.edit_message_text("File Not Found {}".format(downloaded_file_name))

    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="Reply to a Telegram media to /rename with custom thumbnail support",
            reply_to_message_id=update.message_id
        )
        
        
        















        
        
            





















        
        

















    
        
        
        
    
