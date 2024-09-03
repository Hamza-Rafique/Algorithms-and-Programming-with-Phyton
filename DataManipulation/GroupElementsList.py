def GroupElementsList(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

input_list = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1]

print(GroupElementsList(input_list))