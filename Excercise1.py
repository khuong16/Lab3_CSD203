def sum_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_recursive(n - 1)

# Example usage:
n = 5
result = sum_recursive(n)
print(f"The sum of numbers from 1 to {n} is: {result}")
