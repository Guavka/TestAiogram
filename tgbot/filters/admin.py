# Импорт библиотеки для описания типов данных (нужно для документции)
import typing

# Импорт класса на основании которого строятся другие классы фильтров
from aiogram.dispatcher.filters import BoundFilter

# Импорт класса настроек
from tgbot.config import Config


class AdminFilter(BoundFilter):
    key = 'is_main_human' # обязательный ключ для будущего вызова

    def __init__(self, is_main_human: typing.Optional[bool] = None):
        """Функция-конструктор, вызывает 1 раз при создании объекта

        Args:
            is_admin (typing.Optional[bool], optional): _description_. Defaults to None.
        """
        self.is_main_human = is_main_human

    async def check(self, obj):
        """Функция фильтрации. !!!Должна называться так же  и принимать такие же параметры!!!

        Args:
            obj (_type_): бот, которому написали

        Returns:
            bool: Админ написал или нет
        """
        if self.is_main_human is None:
            return False
        config: Config = obj.bot.get('config')
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_main_human
