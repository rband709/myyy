from pyrogram import Client, errors
import logging
from pyrogram.errors import FloodWait , RPCError
import asyncio
#from pyrogram import errors
#import random, os
#from pyrogram import filters, enums 
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#import random, os
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

api_id = 3335796 ,
api_hash = "138b992a0e672e8346d8439c3f42ea78",
bot_token = "5088657122:AAGXARfg6sSX1p1ge876jknkrJizwH959b4"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)
    logger.exception(e)




app.run()
