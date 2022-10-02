from aiogram.types import Message, ChatType
from aiogram.dispatcher import Dispatcher
from aiogram.utils.deep_linking import decode_payload
from aiogram.dispatcher.filters import CommandStart

from re import compile


async def user_start(message: Message):
    await message.reply(f"Hello, {message.from_user.full_name}!")
    await message.answer(f'User id = {message.from_user.id}')


async def user_start_invite(message: Message):
    args = message.get_args()
    payload = decode_payload(args)
    await message.answer(f"Hello, {message.chat.first_name}!\nYou was invited by {payload}")


def register_start(dp: Dispatcher):
    dp.register_message_handler(
        user_start_invite, CommandStart(deep_link=compile(r"[a-zA-Z0-9_-]{12}$")), state="*", chat_type=ChatType.PRIVATE)
    dp.register_message_handler(
        user_start, CommandStart(), state="*", chat_type=ChatType.PRIVATE)
