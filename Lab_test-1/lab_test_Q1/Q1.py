"""Generate Fibonacci sequences with input validation and showcase test cases."""

from typing import List, Union


def fibonacci(n: Union[int, float]) -> List[int]:
    """
    Return the Fibonacci sequence with exactly n terms.

    Args:
        n: Desired length of the Fibonacci sequence. Must be a positive integer.

    Returns:
        List containing Fibonacci numbers up to n terms.

    Raises:
        Returns an error string instead of raising if the input is invalid.
    """

    # Validate type first to prevent processing non-integers
    if not isinstance(n, int):
        return "Error: Positive integer only boss!"

    # Ensure n is strictly positive
    if n <= 0:
        return "Error: Positive integer only boss!"

    # Handle the edge case where only the first term is requested
    if n == 1:
        return [0]

    # Start the sequence with the first two Fibonacci numbers
    sequence = [0, 1]

    # Keep calculating the next term by summing the 2 previous terms
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


if __name__ == "__main__":
    # Eight demonstration test cases covering valid and invalid inputs
    test_inputs = [
        1,          # minimum valid input
        2,          # small valid input
        5,          # typical valid input
        10,         # larger valid input
        20,         # stress valid input
        0,          # invalid non-positive
        -3,         # invalid negative
        3.5,        # invalid non-integer
    ]

    for idx, value in enumerate(test_inputs, start=1):
        # Example: fibonacci(5) -> [0, 1, 1, 2, 3]
        result = fibonacci(value)
        print(f"Test {idx}: fibonacci({value}) -> {result}")


