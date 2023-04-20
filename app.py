import requests
import aiogram
import datetime
import random 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from requests.auth import HTTPBasicAuth



API_TOKEN = '6075492887:AAGHXxcf25JpLInJafQel3xQ9gaBcP6ZsYE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup():
    await message.answer("/start")

@dp.message_handler()
async def cmd_start(message: types.Message):

    kb = [
        [types.KeyboardButton(text="❤️")]
    ]

    
    headers = {'user-agent': 'my-app/0.0.1'}
    
    data = requests.get("https://Val325:G9kT7Gct4AmCsX5MZRhXGMw6@danbooru.donmai.us/posts/random.json", headers=headers)
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    
    
    await bot.send_photo(message.chat.id,reply_markup=keyboard, photo=data.json()['large_file_url'], caption=data.json()['large_file_url'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)