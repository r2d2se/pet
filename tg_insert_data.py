import aiogram

from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from keyboard import start_keyboard

tg_bot = Router()


class Form(StatesGroup):
    FIO = State()
    date_born = State()
    number = State()
    job_title = State()
    departament = State()
    gender = State()
    rights = State()


@tg_bot.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Что нужно сделать?", reply_markup=start_keyboard)


@tg_bot.message(F.text.lower() == "создать напоминание")
async def create_notification(message: types.Message):
    await message.answer("Проверка actions 2", reply_markup=start_keyboard)
