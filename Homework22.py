import string

class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем имена файлов в атрибут file_names
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        # Перебираем каждый файл
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                # Считываем все строки, приводим к нижнему регистру и удаляем пунктуацию
                content = f.read().lower()

                # Удаляем указанные знаки пунктуации
                for p in punctuation:
                    content = content.replace(p, '')

                # Разбиваем строку на слова
                words = content.split()

                # Записываем слова в словарь
                all_words[file_name] = words

        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        # Ищем первое вхождение слова в каждом файле
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # Позиция первого вхождения (индексация с 1)
            else:
                result[name] = None  # Если слово не найдено

        return result

    def count(self, word):
        # Получаем все слова из файлов
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        # Считаем количество вхождений слова в каждом файле
        for name, words in all_words.items():
            result[name] = words.count(word)

        return result


# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('child'))  # Поиск слова 'child'
print(finder.count('child'))  # Подсчёт слова 'child'
