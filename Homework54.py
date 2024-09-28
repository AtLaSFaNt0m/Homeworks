import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Router
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = 'none'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage)


# Define states
class Form(StatesGroup):
    age = State()
    weight = State()
    height = State()


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    calculate_button = KeyboardButton('Рассчитать')
    info_button = KeyboardButton('Информация')
    markup.add(calculate_button, info_button)

    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=markup)


@dp.message_handler(Text(equals='Рассчитать'))
async def main_menu(message: types.Message):
    inline_markup = InlineKeyboardMarkup()
    calories_button = InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
    formulas_button = InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
    inline_markup.add(calories_button, formulas_button)

    await message.answer("Выберите опцию:", reply_markup=inline_markup)


@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Формула Миффлина-Сан Жеора:\n\n"
                              "Для мужчин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) + 5\n"
                              "Для женщин: BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) - 161")


@dp.callback_query_handler(Text(equals='calories'))
async def set_age(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Введите ваш возраст:")
    await Form.age.set()


@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await Form.next()
    await message.answer("Введите ваш вес (кг):")


@dp.message_handler(state=Form.weight)
async def process_weight(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await Form.next()
    await message.answer("Введите ваш рост (см):")


@dp.message_handler(state=Form.height)
async def process_height(message: types.Message, state: FSMContext):
    await state.update_data(height=message.text)

    data = await state.get_data()
    age = data.get('age')
    weight = data.get('weight')
    height = data.get('height')

    await message.answer(f"Ваши данные:\nВозраст: {age} лет\nВес: {weight} кг\nРост: {height} см")

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
