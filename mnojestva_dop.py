def calculate_structure_sum(data):
    sum_data = 0
    for i in data:
        if isinstance(i, (list, tuple, set)):
            sum_data += calculate_structure_sum(i)
        if isinstance(i, dict):
            sum_data += calculate_structure_sum(i.items())
        if isinstance(i, int):
            sum_data += i
        if isinstance(i, str):
            sum_data += len(i)
    return sum_data


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)