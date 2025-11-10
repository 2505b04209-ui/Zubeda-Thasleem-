"""Find largest item in a list with validation and tests.

This module provides `find_largest` which returns the largest numeric value
from a non-empty list or tuple. It includes detailed comments explaining
each line and a set of test cases in `run_tests()` that print expected outputs.
"""

from typing import Union, Sequence

Number = Union[int, float]


def find_largest(seq: Sequence[Number]) -> Number:
    """Return the largest numeric element from a non-empty sequence.

    Args:
        seq (Sequence[Number]): A non-empty sequence (list or tuple) of numbers
            (ints or floats).

    Returns:
        Number: The largest number found in the sequence.

    Raises:
        TypeError: If `seq` is not a list/tuple or contains non-numeric items.
        ValueError: If `seq` is empty.

    Notes:
        - The function performs input validation before computation.
        - It uses a simple linear scan (O(n) time, O(1) extra space).
    """
    # Check that the provided object is a list or tuple (sequence we accept).
    # We avoid accepting arbitrary iterables to keep validation simple.
    if not isinstance(seq, (list, tuple)):
        raise TypeError("Input must be a list or tuple of numbers")

    # Check the sequence is not empty; an empty sequence has no largest element.
    if len(seq) == 0:
        raise ValueError("Input sequence must not be empty")

    # Initialize `largest` with the first element of the sequence.
    # This avoids using None and lets us compare numbers directly.
    largest = seq[0]

    # Validate the first element is numeric (int or float).
    if not isinstance(largest, (int, float)):
        raise TypeError("All items in the sequence must be int or float")

    # Iterate over the remaining items in the sequence starting at index 1.
    # For each item we validate it's numeric then compare with `largest`.
    for i in range(1, len(seq)):
        # Retrieve the current item from the sequence.
        item = seq[i]

        # Check that the current item is a numeric type (int or float).
        if not isinstance(item, (int, float)):
            raise TypeError("All items in the sequence must be int or float")

        # If the current item is greater than `largest`, update `largest`.
        if item > largest:
            largest = item

    # After scanning all items, return the largest found value.
    return largest


def run_tests() -> None:
    """Run example test cases for `find_largest` and print expected outputs.

    This function prints the input, expected output, and the actual output.
    It also demonstrates expected exceptions for invalid inputs.
    """
    print("Running tests for find_largest()")
    print("-" * 50)

    # A list of (input, expected_output) test cases for valid inputs.
    positive_tests = [
        ([3], 3),                    # single element
        ([0, 1, 2, 3], 3),           # ascending
        ([3, 2, 1, 0], 3),           # descending
        ([-5, -1, -3], -1),          # all negative numbers
        ([1.5, 2.5, 0.5], 2.5),      # floats
        ([1, 2.5, 2], 2.5),          # mixed ints and floats
        ([7, 7, 7], 7),              # all equal elements
    ]

    # Run valid-case tests and print results.
    for inp, expected in positive_tests:
        # Print the test case and the expected result.
        print(f"Input: {inp!r} | Expected: {expected!r}")

        # Call the function under test and capture the result.
        result = find_largest(inp)

        # Print the actual result and whether it matches the expectation.
        print(f"Actual:   {result!r} | {'PASS' if result == expected else 'FAIL'}")
        print()

    # Test cases that should raise ValueError (empty sequence).
    print("Testing empty input (expected: ValueError)")
    try:
        find_largest([])
        print("FAIL: expected ValueError for empty list")
    except ValueError as e:
        print(f"PASS: caught expected ValueError -> {e}")
    print()

    # Test cases that should raise TypeError (non-list/tuple input).
    print("Testing non-sequence input (expected: TypeError)")
    try:
        find_largest(123)  # int is not acceptable
        print("FAIL: expected TypeError for non-list input")
    except TypeError as e:
        print(f"PASS: caught expected TypeError -> {e}")
    print()

    # Test cases that should raise TypeError (sequence contains non-numeric).
    print("Testing non-numeric items in sequence (expected: TypeError)")
    try:
        find_largest([1, 'two', 3])
        print("FAIL: expected TypeError for non-numeric items")
    except TypeError as e:
        print(f"PASS: caught expected TypeError -> {e}")
    print()

    print("All tests completed.")


if __name__ == '__main__':
    run_tests()
