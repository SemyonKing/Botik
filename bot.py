import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from config import settings
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from handlers import add_victorina, balance, buy_product, start_bot, proverka_otveta, get_shop, add_product

bot = Bot(token=settings.BT_GET_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(add_victorina.router)
    dp.include_router(start_bot.router)
    dp.include_router(proverka_otveta.router)
    dp.include_router(get_shop.router)
    dp.include_router(add_product.router)
    dp.include_router(buy_product.router)
    dp.include_router(balance.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())