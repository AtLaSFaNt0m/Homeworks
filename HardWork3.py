data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_data_structure(data):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += len(item)
        elif isinstance(item, dict):
            count += len(item)
        elif isinstance(item, tuple):
            count += len(item)
            for sub_item in item:
                if isinstance(sub_item, dict):
                    count += len(sub_item)
        elif isinstance(item, str):
            count += len(item)
        elif isinstance(item, tuple):
            count += len(item)
            for sub_item in item:
                if isinstance(sub_item, tuple):
                    count += len(sub_item)
        else:
            count += 1
    return count

result = calculate_data_structure(data_structure)
print(result)
