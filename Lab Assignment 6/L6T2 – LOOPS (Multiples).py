# =============================================
# TASK 2: Print First 10 Multiples Using Loop
# Prompt: "# Task 2: Function to print first 10 multiples of a number"
# AI Tool: GitHub Copilot (VS Code)
# =============================================

def print_multiples(n):
    """
    Prints the first 10 multiples of a given number.
    Args:
        n (int): The base number
    Logic:
        1. Loop from 1 to 10
        2. Multiply n * i
        3. Print in one line with space
    """
    if n == 0:
        print("Multiples of 0: 0 0 0 0 0 0 0 0 0 0")
        return

    print(f"\nFirst 10 multiples of {n}:")
    # Step 1: Loop from 1 to 10
    for i in range(1, 11):  # range(1,11) → 1 to 10
        multiple = n * i    # Calculate multiple
        print(multiple, end=" ")  # Print horizontally
    print()  # New line at end


# =============================================
# MULTIPLE TEST EXAMPLES
# =============================================
print("="*50)
print("TASK 2: FIRST 10 MULTIPLES – LOOP TEST")
print("="*50)

# Example 1: Multiples of 5
print_multiples(5)

# Example 2: Multiples of 7
print_multiples(7)

# Example 3: Multiples of 10
print_multiples(10)

# Example 4: Multiples of 0 (Edge case)
print_multiples(0)

# Example 5: Negative number
print_multiples(-3)