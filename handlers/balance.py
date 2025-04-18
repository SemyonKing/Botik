from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries.users_table import get_user_points
from queries.list_products_table import get_list_products_table

router = Router()
router.message.filter(
    F.chat.type == "private"
)

@router.message(Command("balance"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    user = message.from_user.username
    if get_user_points(user) != None:
        await message.answer(
        text=f"Ваш баланс: {get_user_points(user)} баллов"
        )
    else:
        await message.answer(
        text=f"Вы ещё не ответили ни на одну викторину. Ваш баланс равен 0"
        )

@router.message(Command("inventory"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    user = message.from_user.username
    list = "В вашем инвентаре:\n"
    for row in get_list_products_table(user):
        list += row + "\n"       
    await message.answer(
        text=list)