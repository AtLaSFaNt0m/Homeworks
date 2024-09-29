import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from crud_functions import initiate_db, add_user, is_included, get_all_products, populate_db

API_TOKEN = 'none'  # Замените на свой токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных и заполнение продуктов
initiate_db()
populate_db()  # Если таблица пуста, продукты будут добавлены


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    calculate_button = KeyboardButton('Рассчитать')
    info_button = KeyboardButton('Информация')
    buy_button = KeyboardButton('Купить')
    register_button = KeyboardButton('Регистрация')
    markup.add(calculate_button, info_button, buy_button, register_button)

    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=markup)


# Регистрация пользователя
@dp.message_handler(Text(equals='Регистрация'))
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
        return

    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом. Введите ещё раз:")
        return

    age = int(age)
    data = await state.get_data()
    username = data['username']
    email = data['email']

    add_user(username, email, age)
    await message.answer(f"Регистрация завершена! Ваши данные:\nИмя: {username}\nEmail: {email}\nВозраст: {age}")

    await state.finish()


# Покупка продуктов
@dp.message_handler(Text(equals='Купить'))
async def get_buying_list(message: types.Message):
    products = get_all_products()

    for product in products:
        product_id, title, description, price = product
        await message.answer(f"Название: {title} | Описание: {description} | Цена: {price} руб")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
