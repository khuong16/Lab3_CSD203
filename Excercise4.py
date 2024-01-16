def is_palindrome_recursive(a, n):
    # Base case: if the array has 0 or 1 elements, it is a palindrome
    if n <= 1:
        return 1
    # Recursive case: check if the first and last elements are equal,
    # and recursively check the subarray without those elements
    else:
        return (a[0] == a[n - 1]) and is_palindrome_recursive(a[1 : n - 1], n - 2)

# Example usage:
array1 = [1, 2, 3, 2, 1]
array2 = [1, 2, 3, 4, 5]

size1 = len(array1)
size2 = len(array2)

result1 = is_palindrome_recursive(array1, size1)
result2 = is_palindrome_recursive(array2, size2)

print(f"Is array1 a palindrome? {result1}")
print(f"Is array2 a palindrome? {result2}")
