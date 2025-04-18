from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries.products_table import insert_products_table, get_product_products_table

class Add_Product(StatesGroup):
    add_name = State()
    add_description = State()
    add_price = State()

router = Router()
router.message.filter(
    F.chat.type == "private",
    F.chat.id == settings.GET_ADMIN_CHAT_ID
)

@router.message(Command("add_product"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    await message.answer(
        text="Напишите имя!"
        )
    await state.set_state(Add_Product.add_name)

@router.message(StateFilter(Add_Product.add_name))
async def start_for_admin(message: types.Message, state: FSMContext):
    msg = message.text.lower()
    if get_product_products_table(msg) != True:
        await state.update_data(name = msg)
        await message.answer(
        text="Напишите описание!"
        )   
        await state.set_state(Add_Product.add_description)   
    else: 
        await message.answer(
        text="Такой продукт уже есть!"
        )
        await state.clear()   

@router.message(StateFilter(Add_Product.add_description))
async def start_for_admin(message: types.Message, state: FSMContext):
    await state.update_data(description = message.text.lower())
    await message.answer(
        text="Напишите cколько стоит!"
        )   
    await state.set_state(Add_Product.add_price)   

@router.message(StateFilter(Add_Product.add_price))
async def start_for_admin(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    
     
    insert_products_table(user_data["name"],user_data["description"],
                           int(message.text.lower()))
    await message.answer(
        text="Добавлен в магазин!"
        )      
    await state.clear()