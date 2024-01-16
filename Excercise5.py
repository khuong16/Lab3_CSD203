def binary_search_recursive(arr, target, low, high):
    # Base case: if low is greater than high, the target is not in the array
    if low > high:
        return -1

    # Calculate the middle index
    mid = (low + high) // 2

    # Check if the target is equal to the element at the middle index
    if arr[mid] == target:
        return mid
    # If the target is smaller, search in the left half of the array
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    # If the target is larger, search in the right half of the array
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 5
target2 = 10

result1 = binary_search_recursive(sorted_array, target1, 0, len(sorted_array) - 1)
result2 = binary_search_recursive(sorted_array, target2, 0, len(sorted_array) - 1)

print(f"Index of target1 in the array: {result1}")
print(f"Index of target2 in the array: {result2}")
