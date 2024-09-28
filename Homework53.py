import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import states
from aiogram.utils import executor

API_TOKEN = 'YOUR_API_TOKEN_HERE'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(states.State):
    age = states.State()
    growth = states.State()
    weight = states.State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Рассчитать', 'Информация']
    keyboard.add(*buttons)
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message: types.Message):
    await Form.age.set()
    await message.answer("Введите ваш возраст:")

@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await Form.next()
    await message.answer("Введите ваш рост в сантиметрах:")

@dp.message_handler(state=Form.growth)
async def process_growth(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await Form.next()
    await message.answer("Введите ваш вес в килограммах:")

@dp.message_handler(state=Form.weight)
async def process_weight(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    user_data = await state.get_data()
    age = user_data.get('age')
    growth = user_data.get('growth')
    weight = user_data.get('weight')
    await message.answer(f"Возраст: {age}, Рост: {growth}, Вес: {weight}")
    await state.finish()

@dp.message_handler(lambda message: message.text not in ['Рассчитать', 'Информация'])
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
