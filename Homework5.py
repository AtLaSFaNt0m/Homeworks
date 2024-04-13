my_list = ['Apple',
           'Pineapple',
           'Melon',
           'Peach',
           'Cucumber',
           'Dragonfruit',
           'Tomato'
           ]
print(my_list, 'Это мой список')
print(my_list[0] + '. Первый элемент списка')
print(my_list[-1] + '. Последний элемент списка')
Aboba = my_list[3:6]
print(Aboba, '- Подсписок 3 и 5 элемента')
my_list[3] = 'City'
print(my_list, ' - Измененный 3 элемент списка')

my_dict = {
    'Apple': 'Яблоко',
    'Pineapple': 'Ананас',
    'Melon': 'Арбуз',
    'Peach': 'Персик',
    'Cucumber': 'Огурчик',
    'Dragonfruit': 'Драконий фрукт'

}
print(my_dict, 'Это мой словарь')
print(my_dict['Apple'], ': Значение слова "Apple"')
my_dict['Pineapple'] = 'ППЭЙПИ'

print(my_dict, ': Измененное значение "Pineapple"')
my_dict.update({
    'Car': 'Машинка',
    'Putin': 'Царь-батюшка',
})
print(my_dict, ':Добавлена пара ключей/значений')