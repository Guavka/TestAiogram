from aiogram import Dispatcher
from tgbot.handlers.private.user.start import register_start
from tgbot.handlers.private.user.help import register_help
from tgbot.handlers.private.user.invite import register_invite
from tgbot.handlers.private.user.menu import register_menu
from tgbot.handlers.private.user.echo import register_echo

def register_user(dp: Dispatcher):
    register_start(dp)
    register_help(dp)
    register_invite(dp)
    register_menu(dp)
    register_echo(dp)
    