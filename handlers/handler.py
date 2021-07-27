from aiogram import types

from data import messages, keyboards
from loader import dp


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(messages.start % message.from_user.full_name, reply_markup=keyboards.menu)
