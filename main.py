import asyncio
import logging
import sys
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message

dispatcher = Dispatcher()
bot = Bot("6551460718:AAGWaCb35zbQ62aPV2KWviHJz-OVMQOdfiU")

@dispatcher.message(CommandStart())
async def command_start_handler(message: Message):
    catButton = [
        [
            types.KeyboardButton(text='Хочу котика!')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=catButton,
        resize_keyboard = True,
        input_field_placeholder='Котики'
    )
    await message.answer(text 'Хочу котика!', reply_markup=keyboard)
@dispatcher.message(F.text == "Хочу котика!")
async def image_handler(message: Message):
    responce = requests.get('https://api.thecatapi.com/v1/images/search').json()
    await message.aswer_photo(responce[0]['url'])
async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())