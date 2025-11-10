def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a given string.
    Case-insensitive: counts both uppercase and lowercase vowels.
    
    Args:
        text (str): The input string to check for vowels
    
    Returns:
        int: The number of vowels found in the text
    
    Raises:
        TypeError: If input is not a string
    """
    # Step 1: Input validation - Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Step 2: Convert to lowercase so we count both upper and lower case vowels
    # For example: 'A' and 'a' are both counted as vowels
    text = text.lower()
    
    # Step 3: Define our vowels list - we'll check each character against these
    vowels = 'aeiou'
    
    # Step 4: Initialize a counter to keep track of vowels found
    count = 0
    
    # Step 5: Loop through each character in the text
    # If the character is a vowel, increment our counter
    for char in text:
        if char in vowels:
            count += 1
            # For example: in "hello"
            # 'h' -> not a vowel, count = 0
            # 'e' -> is a vowel, count = 1
            # 'l' -> not a vowel, count = 1
            # 'l' -> not a vowel, count = 1
            # 'o' -> is a vowel, count = 2
    
    # Step 6: Return the final count
    return count

# Test cases based on the provided examples
def run_tests():
    """Run test cases with the provided example inputs."""
    
    print("=== Vowel Counter Test Cases ===")
    print("-" * 30)
    
    # Test Case 1: "hello" (should find 2 vowels: 'e' and 'o')
    test_str = "hello"
    result = count_vowels(test_str)
    print(f"Text: '{test_str}'")
    print(f"Vowels found: {result}")
    print(f"Expected: 2")
    print()
    
    # Test Case 2: "world" (should find 1 vowel: 'o')
    test_str = "world"
    result = count_vowels(test_str)
    print(f"Text: '{test_str}'")
    print(f"Vowels found: {result}")
    print(f"Expected: 1")
    print()
    
    # Test Case 3: "chatGPT" (should find 1 vowel: 'a')
    test_str = "chatGPT"
    result = count_vowels(test_str)
    print(f"Text: '{test_str}'")
    print(f"Vowels found: {result}")
    print(f"Expected: 1")

# Run the test cases when the script is executed
if __name__ == "__main__":
    run_tests()
