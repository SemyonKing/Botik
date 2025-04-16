from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State
from config import settings

router = Router()
router.message.filter(
    F.chat.type == "private"
)
@router.message(CommandStart())
async def startmessage(message: types.Message):
    if message.chat.id == settings.GET_ADMIN_CHAT_ID:
        await message.answer(
        text="Привет. Я умею создавать викторины и добавлять продукты в магазин\n" \
        "А также буду присылать тебе сообщения, когда кто-то что-то покупает"
        )
    else:
        await message.answer(
        text="Привет. Сдесь ты можешь потратить свои балы"
        )