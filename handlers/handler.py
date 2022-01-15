from aiogram import types

from data import messages, keyboards
from data.models import User
from loader import dp


@dp.message_handler(commands='start')
async def start(message: types.Message):
    User.create(name=message.from_user.full_name)
    await message.answer(messages.start % message.from_user.full_name, reply_markup=keyboards.menu)
