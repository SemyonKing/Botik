from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries.products_table import get_product_products_table, get_product_price_products_table
from queries.users_table import get_user_points, update_user_table
from queries.list_products_table import insert_list_products_table, get_boolean_list_products_table

class Buy_product(StatesGroup):
    vibor = State()


router = Router()
router.message.filter(
    F.chat.type == "private"
)
@router.message(Command("buy"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    await message.answer(
        text="Напишите имя продукта!"
        )
    await state.set_state(Buy_product.vibor)

@router.message(StateFilter(Buy_product.vibor))
async def start_for_admin(message: types.Message, state: FSMContext):
    product = message.text.lower()
    if get_product_products_table(product):
        if get_boolean_list_products_table(message.from_user.username, product) == False:
            pointsPrice = int(get_user_points(message.from_user.username) + int(get_product_price_products_table(product) * -1))
            if pointsPrice >= 0:
                insert_list_products_table(product, message.from_user.username)
                update_user_table(message.from_user.username, int(get_product_price_products_table(product) * -1))
                await message.answer(
                text="Продукт куплен!"
                )
                await message.bot.send_message(
                    chat_id=settings.GET_ADMIN_CHAT_ID,
                    text=f"Пользователь @{message.from_user.username} купил {product}"
                )
            else:
                await message.answer(
                text=f"Вам не хватает: {pointsPrice * -1}"
                )
        else:
            await message.answer(
            text="У вас уже есть такой продукт!"
            ) 
    else:
        await message.answer(
        text="Такого продукта нет!"
        )     
    await state.clear()