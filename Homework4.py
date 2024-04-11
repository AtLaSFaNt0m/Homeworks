mutable_list = ['Aboba', 'Bob', 'Racoon']
print(mutable_list)
mutable_list[0] = 'City'
print(mutable_list)
immutable_var = [(2, 3, 4, 4, 5,), 'string']
print(immutable_var)
immutable_var[0][0] = 2
print(immutable_var)   # Кортеж неизменяемый. Это закон!
