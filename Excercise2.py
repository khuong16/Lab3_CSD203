def find_min_recursive(a, n):
    # Base case: if the array has only one element, it is the minimum
    if n == 1:
        return a[0]
    # Recursive case: find the minimum in the rest of the array and compare with the current element
    else:
        return min(a[n - 1], find_min_recursive(a, n - 1))

# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array_size = len(array)
min_element = find_min_recursive(array, array_size)
print(f"The minimum element in the array is: {min_element}")
