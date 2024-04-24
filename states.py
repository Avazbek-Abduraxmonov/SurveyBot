from aiogram.fsm.state import State, StatesGroup

class surveyBot(StatesGroup):
    name = State()
    surname = State()
    age = State()
    survey = State()
    