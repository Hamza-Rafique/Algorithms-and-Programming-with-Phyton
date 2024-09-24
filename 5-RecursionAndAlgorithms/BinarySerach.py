def binary_search_iterative(arr, target):
    """
    Perform a binary search on a sorted list to find the target value.

    Parameters:
    arr (List[int]): A sorted list of integers.
    target (int): The value to search for.

    Returns:
    int: The index of the target in the list if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search_iterative(arr, target)
print(f"Target found at index: {result}")  # Output: Target found at index: 3
 
    
