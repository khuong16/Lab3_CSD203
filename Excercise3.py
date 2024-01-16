def find_sum_recursive(a, n):
    # Base case: if the array has no elements, the sum is 0
    if n == 0:
        return 0
    # Recursive case: add the current element to the sum of the rest of the array
    else:
        return a[n - 1] + find_sum_recursive(a, n - 1)

# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array_size = len(array)
sum_elements = find_sum_recursive(array, array_size)
print(f"The sum of all elements in the array is: {sum_elements}")
