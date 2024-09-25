import time
from time import sleep
from datetime import datetime
import threading

def write_words(word_count, file_name, start_number):
    with open(file_name, 'a', encoding='utf-8') as file:  # Открытие файла с кодировкой UTF-8
        for i in range(start_number, start_number + word_count):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Вызов функций без потоков и замер времени
start_time = datetime.now()

write_words(10, 'example.txt', 1)
write_words(30, 'example.txt', 11)
write_words(200, 'example.txt', 41)
write_words(100, 'example.txt', 241)

end_time = datetime.now()
print(f"Работа без потоков {end_time - start_time}")

# Создание потоков для выполнения функций
start_time = datetime.now()

threads = []
args_list = [
    (10, 'example.txt', 341),
    (30, 'example.txt', 351),
    (200, 'example.txt', 381),
    (100, 'example.txt', 581)
]

for args in args_list:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

end_time = datetime.now()
print(f"Работа потоков {end_time - start_time}")
