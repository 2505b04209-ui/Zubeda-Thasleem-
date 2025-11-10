def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Check if n is less than 2 (not prime)
    if n < 2:
        return False
    
    # Check if n is 2 (prime)
    if n == 2:
        return True
    
    # Check if n is even (not prime, except for 2)
    if n % 2 == 0:
        return False
    
    # Check odd numbers up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Example usage:
print(is_prime(7))    # True
print(is_prime(15))   # False
print(is_prime(23))   # True
print(is_prime(100))  # False