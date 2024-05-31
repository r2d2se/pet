from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать напоминание")],
        [KeyboardButton(text="Посмотреть напоминания на сегодня")],
        [KeyboardButton(text="Посмотреть все напоминания")],
        [KeyboardButton(text="Удалить последнее напоминание")],
    ],
    resize_keyboard=True,
)

date_picker_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Сегодня, позже")],
        [KeyboardButton(text="Завтра")],
        [KeyboardButton(text="Другая дата")],
    ],
    resize_keyboard=True,
)