def format_name(full_name):
    """
    Format a full name (first and last) as "Last, First".

    Args:
        full_name (str): A string containing exactly two parts: first name and last name.

    Returns:
        str: The formatted name in the form "Last, First".

    Raises:
        TypeError: If `full_name` is not a string.
        ValueError: If `full_name` does not contain exactly two name parts.

    Examples:
        format_name("John Smith") -> "Smith, John"
    """
    # Input validation: ensure the input is a string
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string containing first and last name")

    # Remove leading/trailing whitespace to avoid issues like " John Smith "
    cleaned = full_name.strip()

    # Split the cleaned string on whitespace to separate the name parts
    # For a valid input we expect exactly two parts: first and last
    parts = cleaned.split()

    # If there are not exactly 2 parts, raise an error so the caller knows the input is invalid
    # This helps beginners see that we expect 'First Last' only
    if len(parts) != 2:
        raise ValueError("full_name must contain exactly two words: first and last name")

    # Unpack first and last name from the parts list
    first, last = parts[0], parts[1]

    # Optionally, normalize capitalization: make first letter uppercase and the rest lowercase
    # This handles inputs like 'john SMITH' and formats them as 'Smith, John'
    first_formatted = first.capitalize()
    last_formatted = last.capitalize()

    # Build the final formatted string: "Last, First"
    formatted = f"{last_formatted}, {first_formatted}"

    # Return the formatted name
    return formatted


# Test cases for the required examples
def run_tests():
    """Run the example test cases and print results with explanations."""
    examples = [
        ("John Smith", "Smith, John"),
        ("Emily Johnson", "Johnson, Emily"),
        ("Michael Brown", "Brown, Michael"),
        ("Jessica Williams", "Williams, Jessica"),
        ("David Anderson", "Anderson, David"),
    ]

    print("=== format_name() Test Cases ===")
    print("-" * 34)

    for input_name, expected in examples:
        # Call the function
        result = format_name(input_name)

        # Print the input, the result, and the expected output so beginners can compare
        print(f"Input:  {input_name}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        # Indicate whether the test passed
        print("PASS" if result == expected else "FAIL")
        print()


if __name__ == "__main__":
    run_tests()
