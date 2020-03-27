
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
import os
import time
from pyrogram import Client
from robot.commands import upload_func
from sample_config import Config


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
    
from translation import Translation


thumb_image_path = Config.download_location + "/thumb_image.jpg"

#Here we need to respond to the command /upload to upload on telegram
async def upload_to_tg(bot, message, file_name):
    await asyncio.sleep(1)
    chat_id = message.chat.id
    file = file_name
       
    if os.path.isdir(file_name):
           directory_contents = os.listdir(file_name)
           directory_contents.sort()
           msg = await bot.send_message(message, "Processing ...")
           thumb = None
          
    if os.path.exists(thumb_image_path):
            thumb = thumb_image_path

    if os.path.exists(file_name):
            start = datetime.now()
            c_time = time.time()
            await bot.send_file(
               chat_id = message.chat.id,
               supports_streaming=False,
               thumb = thumb,
               progress_args=(
                    Translation.UPLOAD_START,
                    a, 
                    c_time
               )
            )
            try:
                os.remove(file_name)
            except:
                pass
            
            else:
                await bot.send_message(
                text =Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id = message.chat.id,
                )
       
                





















            






























            
                
                                       
 
    
        
