def flattenList(input_list):
    return [item for sublist in input_list for item in sublist]

nested_list = [[1, 2], [3, 4], [5, 6]]

print(flattenList(nested_list))