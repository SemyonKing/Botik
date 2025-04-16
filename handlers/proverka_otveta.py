from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries import get_questions_table

router = Router()

@router.message()
async def start_for_admin(message: types.Message):
        if get_questions_table(message.text.lower()):
            await message.reply(
            text=f"Это правильный ответ!"
            )

