def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Testing
print("Input: 5 → Output: Factorial =", factorial(5))
print("Input: 0 → Output: Factorial =", factorial(0))