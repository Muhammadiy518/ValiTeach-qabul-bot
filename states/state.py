from aiogram.fsm.state import StatesGroup , State


class BoshmenuKeyboardStates(StatesGroup):
    register = State()
    information = State()


class Register(StatesGroup):
    full_name = State()
    age = State()
    phone_number = State()
    phone_number2 = State()
    week = State()
    time = State()    