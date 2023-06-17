from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, вітаю. З чим можу допомогти?')
    await message.answer_sticker('CAACAgIAAxkBAAMLZIz0ROIeKV5cHYSaiDWUdIdpFOcAAjgLAAJO5JlLMrFH0tlPjNAvBA')


@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(f'Ось id цього стікера:) :\n{message.sticker.file_id}')


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Вибачте, але я вас не зрозумів..')


if __name__ == '__main__':
    executor.start_polling(dp)
