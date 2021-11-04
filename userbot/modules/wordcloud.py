# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the General Public License, Version 3.0;
# you may not use this file except in compliance with the License.
#

import os

import numpy as np
import sys
import traceback
import time
import random
import re
from hachoir.metadata import extractMetadata
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from hachoir.parser import createParser
from PIL import Image
from scipy.ndimage import gaussian_gradient_magnitude
from telethon.tl.types import DocumentAttributeFilename
from wordcloud import ImageColorGenerator, WordCloud

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd


api_id = 8857087  # API ID
api_hash = '55f503a96cfdbac2d30d752d47d5a049'  #API HASH
phone = '+6285866508459'  #NUMBER WITH COUNTRY CODE
timer = 120 #TIME TO WAIT BEFORE NEXT SENDING
msgtosend = "Free Shill 1 Day contact @AmaMarketing" # MESSAGE TO SEND
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
chats = []
last_date = None
chunk_size = 10
groups=[]
result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash = 0
            ))
chats.extend(result.chats)
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
while True:    
    for group in groups:
        try:
            username1 = group.username
            print(username1)    
            client.send_message(username1, msgtosend)
            time.sleep(1)
        except:
            continue 
    print("Send Complete!!, Waiting for " + str(timer) + " seconds")
    time.sleep(timer)
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
