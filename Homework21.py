def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'wb') as file:
        current_position = 0

        for i, line in enumerate(strings, start=1):
            line_bytes = (line + '\n').encode('utf-8')

            file.seek(current_position)
            file.write(line_bytes)
            current_position += len(line_bytes)
            strings_positions[(i, current_position - len(line_bytes))] = line

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
