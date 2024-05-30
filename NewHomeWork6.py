my_dict = {'Иван': 1990, 'Мария': 1985}
print("Исходный словарь my_dict:")
print(my_dict)

print("\nЗначение по ключу 'Иван':", my_dict.get('Иван'))
print("Значение по ключу 'Петр':", my_dict.get('Петр'))

my_dict['Анна'] = 2000
my_dict['Алексей'] = 1995
print("\nСловарь my_dict после добавления произвольных пар:")
print(my_dict)

removed_value = my_dict.pop('Иван')
print("\nУдалено значение по ключу 'Иван':", removed_value)
print("Словарь my_dict после удаления значения:")
print(my_dict)



my_set = {1, 'hello', 3.14, 'hello', (1, 2)}
print("\nИсходное множество my_set:")
print(my_set)

my_set.add('world')
my_set.add(42)
print("\nМножество my_set после добавления элементов:")
print(my_set)

my_set.remove('hello')
print("\nМножество my_set после удаления элемента 'hello':")
print(my_set)

