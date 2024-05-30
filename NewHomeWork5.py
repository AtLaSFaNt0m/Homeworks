immutable_var = (1, 2, 3, 'String', False)
print(f'Immutable tuple: {immutable_var}')
mutable_list = [1, 2, 3, 'Sproink', True]
print(mutable_list)
mutable_list[0] = 'Modified'
print(f'Mutable list: {mutable_list}')

immutable_var[0] = 'Modified' # Кортеж неизменяемый. Это закон!