import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

api_id = 11275039
api_hash = "edf5f943225e77180cf6f0b86718306b"


# user_input_channel = 'https://t.me/CouponBaaz'
user_input_channel = 'https://t.me/CouponBaaz'
subjectFilter = ['loot','LOOT','apple','Apple']
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    # Get message text 
    newMessage = event.message.message
    # Apply 1st round of Regex for Subject for current messageContent - return list of keywords found (case-insensitive) 
    subjectFiltered = re.findall(r"( ?=("+'|'.join(subjectFilter)+r"))", newMessage, re. IGNORECASE),
    if len(subjectFiltered) != 0:
        await client.forward_messages(entity='@G_KA_BOT', messages=event.message)

with client:
    client.run_until_disconnected(),

