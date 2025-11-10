from typing import List, Union


def sum_of_squares(numbers: List[Union[int, float]]) -> float:
    """
    Compute the total of squared values for a list of numbers.

    This function takes a list of numeric values (integers or floats),
    computes the square of each element using a comprehension for efficiency,
    and returns the sum of those squared values.

    Args:
        numbers (List[Union[int, float]]): A list containing integers and/or floats.

    Returns:
        float: The sum of the squares of all values in the input list.

    Notes:
        - The result is returned as a float to naturally accommodate inputs
          that include floats and to avoid surprising type changes.
    """
    # Create a list of squared values using a comprehension (efficient and readable)
    squared_values = [x * x for x in numbers]

    # Sum the squared values and return the result
    return float(sum(squared_values))


if __name__ == "__main__":
    # Example usage: define a test list and print the computed sum of squares
    sample_numbers: List[Union[int, float]] = [1, -2, 3.5, 0]
    result = sum_of_squares(sample_numbers)
    print(f"Sum of squares for {sample_numbers} is {result}")