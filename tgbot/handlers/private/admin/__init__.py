from aiogram import Dispatcher
from tgbot.handlers.private.admin.admin import register_admin as admin_func


def register_admin(dp:Dispatcher):
    admin_func(dp)