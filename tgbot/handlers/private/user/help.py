from aiogram.types import Message, ChatType
from aiogram import Dispatcher


async def user_help(message: Message):
    await message.answer(f'/start - начало работы\n/help - помощь по командам\n/menu - показать меню')


def register_help(dp: Dispatcher):

    dp.register_message_handler(
        user_help, commands=["help"], state="*", chat_type=ChatType.PRIVATE)
