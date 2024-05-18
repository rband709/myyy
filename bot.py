from pyrogram import Client
import logging
from pyrogram.errors import FloodWait , RPCError
import asyncio
from pyrogram import errors
import random, os
from pyrogram import filters, enums 
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random, os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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




@app.on_message(filters.command(["genpassword", 'genpw']))
async def password(client, update):
    message = await update.reply_text(text="`Processing...`")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    if len(update.command) > 1:
        qw = update.text.split(" ", 1)[1]
    else:
        ST = ["5", "7", "6", "9", "10", "12", "14", "8", "13"] 
        qw = random.choice(ST)
    limit = int(qw)
    random_value = "".join(random.sample(password, limit))
    txt = f"<b>Limit:</b> \n<b>Password: <code>random_value</code>"
    btn = InlineKeyboardMarkup([[InlineKeyboardButton('VJ Bots', url='https://t.me/vj_bots')]])
    await message.edit_text(text=txt, reply_markup=btn, parse_mode=enums.ParseMode.HTML)



app.run()
