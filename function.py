from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import *
from buttons import *
from config import *

async def startAnswer(message: Message, bot: Bot):
    await bot.send_message(chat_id=admin_id, text=f"Yangi obunachi: @{message.from_user.username}")
    await message.answer(f"Assalomu Aleykum botimizga xush kelibsiz {message.from_user.full_name}\n\n⏹ Tugmalardan bittasini tanlang", reply_markup=markup)

async def survey_answer(message: Message, bot: Bot, state: FSMContext):
    await message.answer("🤵 Ismingizni kiriting...\n\nMisol: Javohir")
    await state.set_state(surveyBot.name)

async def surveyName(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('❗ Familiyangizni kiriting...\n\nMisol: Valijanov')
    await state.set_state(surveyBot.surname)

async def surveySurname(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(surname = message.text)
    await message.answer('Yoshingizni kiriting')
    await state.set_state(surveyBot.age)

async def surveyAge(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(age = message.text)
    await message.answer('🌍 Kanalimiz qaysi dasturlash tillarni orgatsin!\n\nMisol: Java, Python, Javascript')
    await state.set_state(surveyBot.survey)

async def surveySendGroup(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(survey = message.text)
    data = await state.get_data()
    ariza = (f"Sorovnoma @{message.from_user.username} tomonidan:\n\n"
             f"📛 Ism: {data.get('name')}"
             f"📝 Familiya: {data.get('surname')}"
             f"🎟 Yosh: {data.get('age')}"
             f"🙋‍♂ Haqida: {data.get('survey')}")
    
    await bot.send_message(chat_id=group_id, text=f"{ariza}")
