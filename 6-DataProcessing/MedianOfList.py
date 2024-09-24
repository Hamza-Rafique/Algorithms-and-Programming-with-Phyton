def median_of_list(input_list):
    sorted_list = sorted(input_list)
    length = len(sorted_list)
    if length % 2 == 0:
        median = (sorted_list[length // 2] + sorted_list[length // 2 - 1]) / 2
    else:
        median = sorted_list[length // 2]
    return median

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = median_of_list(numbers)
print(result)  # Output: 5.5
