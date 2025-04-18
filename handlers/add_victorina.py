from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries.questions_table import insert_questions_table, get_question_questions_table, get_answer_questions_table 
from queries.all_tables import clear_tables

class Add_Victorina(StatesGroup):
    add_question = State()
    add_true_answer = State()
    add_points = State()

router = Router()
router.message.filter(
    F.chat.type == "private",
    F.chat.id == settings.GET_ADMIN_CHAT_ID
)
@router.message(Command("clear_database"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    await message.answer(
        text="Начинаю чистить!"
        )
    try:
        clear_tables()
        await message.answer(
        text="Очистил!"
        )
    except Exception as e: await message.answer(
        text=f"Не удалось очистить! Ошибка: {e}"
        )

@router.message(Command("add_victorina"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    await message.answer(
        text="Напишите вопрос!"
        )
    await state.set_state(Add_Victorina.add_question)

@router.message(StateFilter(Add_Victorina.add_question))
async def start_for_admin(message: types.Message, state: FSMContext):
    msg = message.text.lower()
    if get_question_questions_table(msg) != msg:
        await state.update_data(vopros = msg)
        await message.answer(
        text="Напишите правильный ответ!"
        )   
        await state.set_state(Add_Victorina.add_true_answer)
    else: 
        await message.answer(
        text="Такой вопрос уже есть!"
        )
        await state.clear()      

@router.message(StateFilter(Add_Victorina.add_true_answer))
async def start_for_admin(message: types.Message, state: FSMContext):
    msg = message.text.lower()
    if get_answer_questions_table(msg) != msg:
        await state.update_data(otvet = msg)
        await message.answer(
        text="Напишите сколько очков!"
        )   
        await state.set_state(Add_Victorina.add_points)  
    else: 
        await message.answer(
        text="Такой ответ уже есть!"
        )
        await state.clear()   

@router.message(StateFilter(Add_Victorina.add_points))
async def start_for_admin(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    mуmsg = message.text.lower()

    await message.answer(
        text="Отправлено в группу!"
        )   
    msg = await message.bot.send_message(
        chat_id=settings.GET_CHAT_ID,
        text=f"{user_data["vopros"]}\nБаллов за ответ: {mуmsg}"
    )
    insert_questions_table(msg.message_id,user_data["vopros"],user_data["otvet"],
                           int(mуmsg))    
    await state.clear()