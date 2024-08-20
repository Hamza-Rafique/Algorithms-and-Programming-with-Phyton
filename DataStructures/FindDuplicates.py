def find_duplicates(input_list):
    element_count = {}
    duplicates = []

    for item in input_list:
        if item in element_count:
            element_count[item] +=1
        else:
            element_count[item] = 1
    
    for item, count in element_count.items():
     if count > 1:
        duplicates.append(item)
    return duplicates


input_list = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1]
duplicates = find_duplicates(input_list)
print("Duplicates in the list:", duplicates)