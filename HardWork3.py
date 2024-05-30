def calculate_structure_sum(data_structure):
    def helper(element):
        total = 0
        if isinstance(element, int):
            total += element
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            for item in element:
                total += helper(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                total += helper(key)
                total += helper(value)
        return total

    return helper(data_structure)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
