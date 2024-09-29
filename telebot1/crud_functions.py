import sqlite3


# Функция для инициализации базы данных и создания таблиц
def initiate_db():
    """Создаем таблицы Products и Users, если они еще не существуют."""
    conn = sqlite3.connect('shop.db')  # Подключаемся к базе данных (или создаем файл, если его нет)
    cursor = conn.cursor()

    # Создаем таблицу Products, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    # Создаем таблицу Users, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')

    conn.commit()
    conn.close()


# Функция для добавления продуктов в базу данных, если она пуста
def populate_db():
    """Заполняем таблицу Products продуктами, если она пуста."""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    # Проверяем, есть ли записи в таблице Products
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]

    if count == 0:
        # Массив продуктов для добавления в таблицу
        products = [
            ('Product1', 'Описание продукта 1', 100),
            ('Product2', 'Описание продукта 2', 200),
            ('Product3', 'Описание продукта 3', 300),
            ('Product4', 'Описание продукта 4', 400)
        ]

        # Добавляем продукты в таблицу
        cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
        conn.commit()
        print("Продукты успешно добавлены в базу данных.")
    else:
        print("Таблица продуктов уже содержит данные.")

    conn.close()


# Функция для получения всех продуктов
def get_all_products():
    """Возвращаем все записи из таблицы Products."""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Функция для добавления нового пользователя
def add_user(username, email, age):
    """Добавляем пользователя в таблицу Users."""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Users (username, email, age, balance)
    VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()


# Функция для проверки, есть ли пользователь с данным именем
def is_included(username):
    """Проверяем, существует ли пользователь с данным именем."""
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


# Вызов функций для инициализации базы данных и заполнения продуктов
if __name__ == '__main__':
    initiate_db()  # Создаем базу данных и таблицы
    populate_db()  # Заполняем базу данных продуктами
