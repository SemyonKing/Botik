from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries import insert_questions_table

class Add_Victorina(StatesGroup):
    add_question = State()
    add_true_answer = State()
    add_points = State()

router = Router()
router.message.filter(
    F.chat.type == "private"
)
@router.message(Command("add_victorina"), StateFilter(None))
async def start_for_admin(message: types.Message, state: FSMContext):
    await message.answer(
        text="Напишите вопрос!"
        )
    await state.set_state(Add_Victorina.add_question)

@router.message(StateFilter(Add_Victorina.add_question))
async def start_for_admin(message: types.Message, state: FSMContext):
    await state.update_data(vopros = message.text.lower())
    await message.answer(
        text="Напишите правильный ответ!"
        )   
    await state.set_state(Add_Victorina.add_true_answer)   

@router.message(StateFilter(Add_Victorina.add_true_answer))
async def start_for_admin(message: types.Message, state: FSMContext):
    await state.update_data(otvet = message.text.lower())
    await message.answer(
        text="Напишите сколько очков!"
        )   
    await state.set_state(Add_Victorina.add_points)   

@router.message(StateFilter(Add_Victorina.add_points))
async def start_for_admin(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    insert_questions_table(user_data["vopros"],user_data["otvet"],
                           int(message.text.lower()))
    await message.answer(
        text="Отправлено в группу!"
        )   
    await message.bot.send_message(
        chat_id=settings.GET_CHAT_ID,
        text=f"{user_data["vopros"]}"
    )    
    await state.clear()