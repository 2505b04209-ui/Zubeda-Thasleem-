# -------------------------------------------------------------------
# Task 3 - Transparency
# Topic: Fibonacci number using recursion with full explanation
# -------------------------------------------------------------------

# Function: fibonacci(n)
# Purpose:  To return the nᵗʰ Fibonacci number.
# The Fibonacci series: 0, 1, 1, 2, 3, 5, 8, ...
# Each number = sum of previous two numbers.
# Example: fibonacci(5) → 5  (sequence: 0,1,1,2,3,5)

def fibonacci(n):
    """
    Recursive function to find nth Fibonacci number.
    Base cases:
        if n == 0 → return 0
        if n == 1 → return 1
    Recursive case:
        return fibonacci(n-1) + fibonacci(n-2)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------------------------------------------------
# Example run section
# -------------------------------------------------------------------
# We will calculate first 10 Fibonacci numbers
print("Fibonacci sequence for first 10 terms:")
for i in range(10):
    print(f"Term {i}: {fibonacci(i)}")

# -------------------------------------------------------------------
# Transparent Explanation:
# -------------------------------------------------------------------
print("\nExplanation:")
print("1. Function uses recursion — function calls itself.")
print("2. Base cases stop infinite recursion (when n=0 or n=1).")
print("3. Each call adds results of previous two terms.")
print("4. The printed series helps verify correctness.")
