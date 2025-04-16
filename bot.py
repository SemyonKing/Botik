import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from config import settings
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from handlers import add_victorina, start_bot, proverka_otveta

bot = Bot(token=settings.BT_GET_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(add_victorina.router)
    dp.include_router(start_bot.router)
    dp.include_router(proverka_otveta.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())