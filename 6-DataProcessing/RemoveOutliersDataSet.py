def remove_outliers(data_set):
    data_set = sorted(data_set)
    q1 = data_set[len(data_set) // 4]
    q3 = data_set[len(data_set) * 3 // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data_set if lower_bound <= x <= upper_bound]

# Example usage:
data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_outliers(data_set)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]