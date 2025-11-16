# =============================================
# LAB 9.3 – TASK 1: Sum of Even & Odd Numbers
# AI Tool
# =============================================

def sum_even_odd(numbers):
    """
    Calculate and return the sum of even and odd numbers in a list.

    This function takes a list of integers and separates them into even and odd.
    It then computes the sum of each group and returns both sums as a tuple.

    Args:
        numbers (list of int): A list containing integer values.
            Example: [1, 2, 3, 4, 5]

    Returns:
        tuple: A tuple containing two integers:
            - First element: Sum of all even numbers
            - Second element: Sum of all odd numbers

    Raises:
        TypeError: If input is not a list or contains non-integer values.

    Examples:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)

        >>> sum_even_odd([10, 20, 30])
        (60, 0)

        >>> sum_even_odd([-1, -2, 3, 4])
        (2, 2)

        >>> sum_even_odd([0])
        (0, 0)

        >>> sum_even_odd([])
        (0, 0)

        >>> sum_even_odd([7, 7, 7, 7])
        (0, 28)

        >>> sum_even_odd([2, 4, 6, 8, 10, 12])
        (42, 0)

        >>> sum_even_odd([1, 3, 5, 7, 9, 11, 13, 15])
        (0, 64)
    """
    # Input validation: Ensure input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Initialize sums
    even_sum = 0   # Will store sum of even numbers
    odd_sum = 0    # Will store sum of odd numbers

    # Loop through each number in the list
    for num in numbers:
        # Check if number is integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")

        # Check if number is even (divisible by 2)
        if num % 2 == 0:
            even_sum += num   # Add to even sum
        else:
            odd_sum += num    # Add to odd sum

    # Return both sums as a tuple
    return even_sum, odd_sum


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    examples = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [-1, -2, 3, 4],
        [0],
        [],
        [7, 7, 7, 7],
        [2, 4, 6, 8, 10, 12],
        [1, 3, 5, 7, 9, 11, 13, 15]
    ]

    print("8 EXAMPLES – SUM OF EVEN & ODD NUMBERS\n" + "="*50)
    for i, nums in enumerate(examples, 1):
        even, odd = sum_even_odd(nums)
        print(f"{i}. Input: {nums}")
        print(f"    Even Sum: {even} | Odd Sum: {odd}\n")