def print_params(a=1, b='String', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])


value_list = [4, 2, 3]
values_dict = {'a': 132, 'b': 'Aboba', 'c': False}


print_params(*value_list)
print_params(**values_dict)
