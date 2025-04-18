from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries.products_table import get_products_table

router = Router()
router.message.filter(
    F.chat.type == "private"
)

@router.message(Command("shop"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    list = get_products_table()
    msg = ""
    for row in list:
        msg = msg + row + "\n"
    await message.answer(
        text=msg
        )


