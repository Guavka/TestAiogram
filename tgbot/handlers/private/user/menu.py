from aiogram.types import Message, ChatType
from aiogram import Dispatcher
from tgbot.keyboards.reply import main_menu
from aiogram.utils.markdown import hbold, hlink


async def user_menu(message: Message):
    await message.answer(text='Выберите пункт меню:', reply_markup=main_menu)


async def user_menu_1(message: Message):
    title = hbold('Малая Компьютерная Академия')
    link = hlink('Узнать обо всех формах обучения',
                 'https://www.donstep.com/formy-obucheniya/')
    await message.answer(text=f'{title}\n\nМалая Компьютерная Академия – это компьютерное образование для детей 7-14 лет, \
позволяющее ребенку извлечь максимальную пользу из времени, проведенного за компьютером.\nВ Малой Компьютерной Академии школьники получают \
практические навыки и теоретические знания.\nПреподаватели-практики научат детей разрабатывать интернет-сайты, моделировать и программировать \
роботов, создавать собственные игры, анимировать персонажей, безопасно работать с поисковыми системами, проводить фото- и видеосъемку.\nОбъем \
полученных знаний поможет вашему ребенку сделать ранний старт в IT, опередив сверстников в будущем профессиональном развитии.\nКомпьютер \
перестанет быть для ребенка просто игрушкой, а станет инструментом для создания собственных проектов, которые могут вырасти до уровня всемирно \
известных стартапов.\n\n{link}',
                         reply_markup=main_menu)


async def user_menu_2(message: Message):
    await message.answer(text='Выберите пункт меню:')


async def user_menu_3(message: Message):
    await message.answer(text='Выберите пункт меню:')


def register_menu(dp: Dispatcher):

    dp.register_message_handler(
        user_menu, commands=["menu"], state="*", chat_type=ChatType.PRIVATE)
    dp.register_message_handler(
        user_menu_1, text='Малая академия', chat_type=ChatType.PRIVATE)
