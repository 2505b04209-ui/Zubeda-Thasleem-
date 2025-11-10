# =============================================
# TASK 4: LOOPS – Sum of First n Natural Numbers
# Prompt: "Write function to calculate sum of first n numbers using for and while loops"
# AI Tool: GitHub Copilot (VS Code)
# =============================================

def sum_to_n_for(n):
    """
    Calculate sum of first n natural numbers using FOR loop.
    
    Args:
        n (int): Positive integer (n >= 1)
    
    Returns:
        int: Sum = 1 + 2 + 3 + ... + n
    
    Logic:
        - Start total = 0
        - Loop i from 1 to n (inclusive)
        - Add each i to total
        - Return final sum
    
    Why range(1, n+1)?
        → range(1, n+1) → generates 1, 2, ..., n
        → If range(1, n) → stops at n-1 → WRONG!
    """
    # Step 1: Input validation
    if not isinstance(n, int) or n < 1:
        print("Error: n must be a positive integer!")
        return 0

    # Step 2: Initialize sum
    total = 0
    
    # Step 3: For loop – Clean and Pythonic
    for i in range(1, n + 1):  # Includes n!
        total += i             # total = total + i
        # Optional: print(f"Adding {i} → total = {total}")
    
    # Step 4: Return result
    return total


def sum_to_n_while(n):
    """
    Calculate sum of first n natural numbers using WHILE loop.
    
    Args:
        n (int): Positive integer
    
    Returns:
        int: Sum = 1 + 2 + ... + n
    
    Logic:
        - Start i = 1, total = 0
        - While i <= n → add i to total
        - Increment i by 1 each time
        - CRITICAL: i += 1 → Prevents infinite loop!
    """
    # Step 1: Input validation
    if not isinstance(n, int) or n < 1:
        print("Error: n must be a positive integer!")
        return 0

    # Step 2: Initialize variables
    total = 0
    i = 1

    # Step 3: While loop – Manual control
    while i <= n:              # Condition: i must not exceed n
        total += i             # Add current number
        i += 1                 # CRITICAL: Increment i
        # Without i += 1 → Infinite loop!
    
    # Step 4: Return result
    return total


# =============================================
# MULTIPLE TEST EXAMPLES (Including Edge Cases)
# =============================================
print("\n" + "="*60)
print("TASK 4: SUM OF FIRST n NUMBERS – FOR vs WHILE LOOP")
print("="*60)

# Example 1: Normal case
print("1. Sum to 10 (for loop):  ", sum_to_n_for(10))      # Expected: 55
print("   Sum to 10 (while loop):", sum_to_n_while(10))   # Expected: 55

# Example 2: Larger number
print("\n2. Sum to 100:")
print("   For loop:  ", sum_to_n_for(100))    # 5050
print("   While loop:", sum_to_n_while(100))  # 5050

# Example 3: n = 1 (Minimum valid)
print("\n3. Edge Case: n = 1")
print("   For:  ", sum_to_n_for(1))   # 1
print("   While:", sum_to_n_while(1)) # 1

# Example 4: n = 0 (Invalid)
print("\n4. Invalid Input: n = 0")
print("   For:  ", sum_to_n_for(0))   # Error + 0
print("   While:", sum_to_n_while(0)) # Error + 0

# Example 5: Negative (Invalid)
print("\n5. Invalid: n = -5")
print("   For:  ", sum_to_n_for(-5))
print("   While:", sum_to_n_while(-5))

# Example 6: Formula check (Gauss's formula)
n = 70
expected = n * (n + 1) // 2
print(f"\n6. Gauss Formula Check (n={n}): {expected}")
print(f"   For loop result:  {sum_to_n_for(n)}")   # Must match
print(f"   While loop result: {sum_to_n_while(n)}") # Must match