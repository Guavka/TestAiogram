from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Малая академия')
        ],
        [
            KeyboardButton(text='Програмирование'),
            KeyboardButton(text='Дизайн')
        ],
        [
            KeyboardButton(text='Курсы')
        ],
    ],
    resize_keyboard=True
)
