from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply(f"Hello, {message.from_user.full_name}!")
    await message.answer(f'User id = {message.from_user.id}')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
