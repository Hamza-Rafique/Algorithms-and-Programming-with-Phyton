def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
if __name__ == "__main__":
    sample_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = quick_sort(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Sorted list: {sorted_list}")
