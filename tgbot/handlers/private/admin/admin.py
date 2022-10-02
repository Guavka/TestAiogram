# Импорт класса Dispatcher (обработчик) - отвечат за всю работу бота (чтение, ответы, меню и прочее)
from aiogram import Dispatcher

# Импорт aiogram.types. В данном случае Message - класс текстовых сообщений
from aiogram.types import Message, ChatType


async def admin_start(message: Message):
    """Функция-хендлер, которая отвечает пользователю на сообщение

    Args:
        message (Message): объект сообщения
    """
    await message.reply("Hello, admin!")  # бот отвечает админу с пересланным сообщением
    await message.answer("Hello, admin!")  # бот отвечает админу


async def admin_end(message: Message):
    """Функция-хендлер, которая отвечает пользователю на сообщение

    Args:
        message (Message): объект сообщения
    """
    await message.reply("Bye, admin!")  # бот отвечает админу с пересланным сообщением
    await message.answer("Bye, admin!")  # бот отвечает админу


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=[
                                "start"], state="*", is_main_human=True, chat_type=ChatType.PRIVATE)
    dp.register_message_handler(admin_end, commands=[
                                "end"], state="*", is_main_human=True, chat_type=ChatType.PRIVATE)
