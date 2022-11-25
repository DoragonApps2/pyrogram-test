from pyrogram import Client, filters
from pyrogram.types import Message
bot = Client(
    name='pyrogram-test',
    api_id=13543479,
    api_hash='809445ffd79aefa06a50255e38b95ca3',
    bot_token='5509172033:AAHKR7wLkaG-awY6nu4-fcuiXLvwOSiEVto'
)


#                              COMANDOS USERS

@bot.on_message(filters.command('start') & filters.private)
def command_start(client, msg: Message):
    msg.reply("hola")
    

#                               BOT READY

def run():
    bot.run(print('bot ready'))

run()
