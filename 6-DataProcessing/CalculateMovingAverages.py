def moving_average(numbers, window_size):
    if not numbers or window_size <= 0:
        return []

    moving_averages = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        window_average = sum(window) / window_size
        moving_averages.append(window_average)
    
    return moving_averages

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3
result = moving_average(numbers, window_size)
print(result)  # Output: [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
