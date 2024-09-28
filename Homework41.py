import requests
import matplotlib.pyplot as plt
import pandas as pd

#1. Отправляем GET-запрос к API
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

#2. Выводим статус ответа и текст
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

#3. Преобразуем ответ в JSON-формат
data = response.json()
print(f"Title: {data['title']}")
# Возможности библиотеки requests значительно упрощают взаимодействие с веб-ресурсами,
# предоставляя простой и интуитивно понятный интерфейс для отправки HTTP-запросов.
# С её помощью можно легко получать данные с различных API и сайтов,
# автоматизируя процессы работы с веб-данными.



#1. Создание DataFrame из словаря
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

#2. Вывод первых строк DataFrame
print(df.head())

#3. Фильтрация данных по условию
adults = df[df['Age'] > 29]
print(adults)

#4. Чтение данных из CSV-файла
#df = pd.read_csv('data.csv')  # Пример чтения файла CSV
#упрощает манипуляции с данными и анализ, предлагая удобные методы для выборки,
#фильтрации и агрегации информации.


#1. Данные для графика
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 18]

#2. Построение линейного графика
plt.plot(x, y, label='Data Line', color='blue', marker='o')

#3. Добавление заголовка и подписей осей
plt.title('Sample Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

#4. Добавление легенды и отображение графика
plt.legend()
plt.show()

#Эта библиотека является стандартом в сообществе Python
#для построения графиков и интегрируется с другими библиотеками