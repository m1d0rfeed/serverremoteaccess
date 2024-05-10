
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from subprocess import check_output

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)
client_credentials = {}  

YOUR_SERVER_CHAT_ID = YOUR_CHAT_ID_HERE

@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_message(message: types.Message):
    if message.chat.id == YOUR_SERVER_CHAT_ID:
        command = message.text
        try:
            output = f"{check_output(command, shell=True)}"
            await bot.send_message(message.chat.id, output)
        except:
            await bot.send_message(message.chat.id, "Invalid input")

async def on_startup(dp):
    await bot.send_message(YOUR_SERVER_CHAT_ID, "Bot started")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    dp.loop.create_task(on_startup(dp))
    loop.run_forever()
