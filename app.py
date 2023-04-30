import requests
import aiogram
import datetime
import random 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from requests.auth import HTTPBasicAuth
from aiogram.types import ParseMode
from aiogram.utils import executor


API_TOKEN = '6075492887:AAGHXxcf25JpLInJafQel3xQ9gaBcP6ZsYE'

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

kb = [
        [types.KeyboardButton(text="❤️")],
        [types.KeyboardButton(text="🔞")]
    ]

 


async def on_startup():
    await message.answer("/start")

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):

    headers = {'user-agent': 'my-app/0.0.1'}
    
    data = requests.get("https://Val325:G9kT7Gct4AmCsX5MZRhXGMw6@danbooru.donmai.us/posts/random.json?post[rating]=g", headers=headers)
    
    print(data.json())
    id_post = data.json()['id']
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await bot.send_photo(message.chat.id,reply_markup=keyboard, photo=data.json()['large_file_url'], caption=f'post: https://danbooru.donmai.us/posts/{id_post}')

#Usual
@dp.message_handler(Text(equals="❤️"))
async def general_h(message: types.Message):

    headers = {'user-agent': 'my-app/0.0.1'}
    
    data = requests.get("https://Val325:G9kT7Gct4AmCsX5MZRhXGMw6@danbooru.donmai.us/posts/random.json?tags=rating%3Ag", headers=headers)
    
    print(data.json())
    id_post = data.json()['id']
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    #
    
    await bot.send_photo(message.chat.id,reply_markup=keyboard, photo=data.json()['large_file_url'], caption=f'post: https://danbooru.donmai.us/posts/{id_post}')

#+18 content
@dp.message_handler(Text(equals="🔞"))
async def sensitive_handler(message: types.Message):

    headers = {'user-agent': 'my-app/0.0.1'}
    
    data = requests.get("https://Val325:G9kT7Gct4AmCsX5MZRhXGMw6@danbooru.donmai.us/posts/random.json?tags=rating%3Aquestionable", headers=headers)
    
    print(data.json())
    id_post = data.json()['id']
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    #
    
    await bot.send_photo(message.chat.id,reply_markup=keyboard, photo=data.json()['large_file_url'], caption=f'post: https://danbooru.donmai.us/posts/{id_post}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)