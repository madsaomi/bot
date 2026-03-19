import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
)
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise RuntimeError('Missing required environment variable: TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menu')],
        [KeyboardButton(text='Contact')],
        [KeyboardButton(text='Help')],
    ],
    resize_keyboard=True,
)

links_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Google', url='https://www.google.com/')],
        [InlineKeyboardButton(text='Telegram', url='https://web.telegram.org/')],
    ]
)


@dp.message(Command(commands=['start']))
async def cmd_start(message: Message) -> None:
    """Greet the user and show the main menu."""
    await message.answer(
        'Assalomu alaykum, botimizga xush kelibsiz!',
        reply_markup=main_keyboard,
    )


@dp.message(Command(commands=['menu']))
async def cmd_menu(message: Message) -> None:
    """Show the menu keyboard."""
    await message.answer("Bu yerda menyu bo'ladi", reply_markup=main_keyboard)


@dp.message(Command(commands=['contact']))
async def cmd_contact(message: Message) -> None:
    """Share contact links with the user."""
    await message.answer("Bu yerda kontaktlar bo'ladi", reply_markup=links_keyboard)


@dp.message(Command(commands=['help']))
async def cmd_help(message: Message) -> None:
    """Show help information."""
    await message.answer("Bu yerda yordam bo'ladi", reply_markup=main_keyboard)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
