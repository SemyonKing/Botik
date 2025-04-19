from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings
from queries.questions_table import get_bool_questions_table, get_poins_questions_table, get_msg_id_questions_table, get_question_answer_questions_table, update_user_question_table
from queries.users_table import get_bool_user_table, update_user_table, insert_users_table

router = Router()

router.message.filter(
    F.chat.type != "private"
)
@router.message()
async def start_for_admin(message: types.Message):
        msg = message.text.lower()
        if get_bool_questions_table(msg) == False:
            await message.reply(
            text=f"Это правильный ответ!"
            )
            await message.bot.edit_message_text(chat_id=settings.GET_CHAT_ID,
                                          message_id=get_msg_id_questions_table(msg),
                                          text=f"{get_question_answer_questions_table(msg)}\nБаллов за ответ: {get_poins_questions_table(msg)}\n#найденОтвет Правильный ответ: {msg}")  
            
            if get_bool_user_table(message.from_user.id):
                  update_user_table(message.from_user.id, get_poins_questions_table(msg))                  
            else:
                  insert_users_table(message.from_user.username, message.from_user.id, get_poins_questions_table(msg))
            update_user_question_table(msg, message.from_user.id)
        
            


