def factorial_iterative(n):
    """Calculate the factorial of a non-negative integer using iteration.

    Args:
        n (int): A non-negative integer to calculate factorial for.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Initialize result to 1 (base case)
    result = 1
    
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    
    return result

def factorial_recursive(n):
    """Calculate the factorial of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer to calculate factorial for.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base cases: 0! = 1 and 1! = 1
    if n <= 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

# Test cases
def run_tests():
    """Run test cases for both factorial functions."""
    test_cases = [
        (0, 1),    # Edge case: 0! = 1
        (1, 1),    # Edge case: 1! = 1
        (5, 120),  # Normal case: 5! = 120
        (10, 3628800)  # Larger number
    ]
    
    print("Testing factorial functions...")
    print("-" * 40)
    
    for n, expected in test_cases:
        # Test iterative version
        iter_result = factorial_iterative(n)
        print(f"Iterative {n}! = {iter_result} {'✓' if iter_result == expected else '✗'}")
        
        # Test recursive version
        rec_result = factorial_recursive(n)
        print(f"Recursive {n}! = {rec_result} {'✓' if rec_result == expected else '✗'}")
        print()
    
    # Test error cases
    try:
        factorial_iterative(-1)
    except ValueError as e:
        print("Negative input test passed ✓")
    
    try:
        factorial_iterative(3.14)
    except TypeError as e:
        print("Non-integer input test passed ✓")

if __name__ == "__main__":
    run_tests()