def factorial_iterative(n):
    """
    Calculate factorial using a loop.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: n! (factorial of n)
    
    Raises:
        ValueError: If n is negative
    """
    # Step 1: Check if input is negative
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Step 2: Start with 1 (0! and 1! = 1)
    result = 1
    
    # Step 3: Multiply from 1 to n
    for i in range(1, n + 1):
        result *= i  # result = result * i
    
    # Step 4: Return final result
    return result


def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: n!
    
    Raises:
        ValueError: If n is negative
    """
    # Step 1: Validate input
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Step 2: Base case – 0! and 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Step 3: Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


# === TEST CASES ===
print("5! (iterative):", factorial_iterative(6))      # Expected: 120
print("5! (recursive):", factorial_recursive(5))      # Expected: 120
# print(factorial_iterative(-1))  # Raises ValueError