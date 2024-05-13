from aiogram import Bot, types, Dispatcher, F
from aiogram.filters import CommandStart, Command
from function import *
from config import *
from states import *
from asyncio import run

dp = Dispatcher()

async def adminStartAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot ishga tushdi ✅")

async def adminShutdownAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot ishdan to'xtadi ❌")

async def start():
    dp.startup.register(adminStartAnswer)
    dp.message.register(startAnswer, CommandStart())
    dp.message.register(survey_answer, F.text == "So'rovnoma to'ldirish!")
    dp.message.register(surveyName, surveyBot.name)
    dp.message.register(surveySurname, surveyBot.surname)
    dp.message.register(surveyAge, surveyBot.age)
    dp.message.register(surveySendGroup, surveyBot.survey)

    dp.shutdown.register(adminShutdownAnswer)

    bot = Bot(token=token)
    await dp.start_polling(bot, polling_timeout=1)
run(start())