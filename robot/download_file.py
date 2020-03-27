
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


import asyncio
import os
import requests
from time import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
    
from translation import Translation


#Here We need to detect the file size of the download file from url
async def detect_file_size(url):
        req = requests.get(url, allow_redirects=True, stream=True)
        total_size = int(r.headers.get("content-length", 0))
        return total_size

#Here we are downloading the file
async def download_file(url):
        print("Download starting....")
        await asyncio.sleep(2)
        req = requests.get(url, allow_redirects=True, stream=True)
        file_name = os.path.basename(url)
        total_size = int(r.headers.get("content-length", 0))
        downloaded_size = 0

        with open (file_name, "wb") as f:
                for chunk in req.iter_content(chunk_size = 1024):
                        f.write(chunk)
                        downloaded_size += chunk_size

        return "Download completed: " + file_name
                        
        
        
