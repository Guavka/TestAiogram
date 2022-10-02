from aiogram import Dispatcher
from aiogram.types import BotCommand


async def init_base_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        BotCommand('start', 'Начало работы'),
        BotCommand('help', 'Помощь по командам'),
        BotCommand('menu', 'Вывод меню'),
        BotCommand('invite', 'Сгенерировать ссылку для рефералов'),
    ])
