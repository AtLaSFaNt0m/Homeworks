import sqlite3

# Connect to the database
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Create the Users table if it doesn't exist
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Clear the Users table
cursor.execute('DELETE FROM Users')

# User data to be inserted
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

# Insert users into the table
cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)

# Update every second user starting from the first to have a balance of 500
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

# Delete every third user starting from the first
# This will delete users with id 1, 4, 7, and 10
cursor.execute('DELETE FROM Users WHERE id IN (SELECT id FROM Users WHERE id % 3 = 1)')

# Delete user with id=6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Fetch remaining user data
cursor.execute('SELECT username, email, age, balance FROM Users')
users_data = cursor.fetchall()

# Print remaining users
print("Remaining Users:")
for user in users_data:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# Calculate average balance using AVG function
cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()[0]

# Print average balance
if average_balance is not None:
    print(f"Средний баланс: {average_balance:.2f}")
else:
    print("Нет пользователей для расчета среднего баланса.")

# Commit changes and close the connection
conn.commit()
conn.close()
