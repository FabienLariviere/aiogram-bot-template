from aiogram import types
from loader import dp, db

import data.messages as messages
import data.keyboards as keyboards
from data.config import ADMINS

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(messages.start, reply_markup=keyboards.menu)

