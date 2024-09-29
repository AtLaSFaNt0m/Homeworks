# crud_functions.py
import sqlite3


# Функция для создания таблицы Products, если она не существует
def initiate_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Функция для заполнения таблицы Products
def populate_db():
    # Инициализация базы данных, создание таблицы Products, если её нет
    initiate_db()

    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Данные для заполнения таблицы
    products = [
        ('Product1', 'Описание продукта 1', 100),
        ('Product2', 'Описание продукта 2', 200),
        ('Product3', 'Описание продукта 3', 300),
        ('Product4', 'Описание продукта 4', 400),
    ]

    # Вставка данных в таблицу Products
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)

    # Сохранение изменений
    conn.commit()

    # Закрытие подключения
    conn.close()


# Вызов функции для заполнения таблицы продуктами
if __name__ == '__main__':
    populate_db()
