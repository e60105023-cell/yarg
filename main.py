from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import os

TOKEN = os.getenv("BOT_TOKEN")  # берём токен из переменной окружения
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я эхо-бот.")

@router.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



