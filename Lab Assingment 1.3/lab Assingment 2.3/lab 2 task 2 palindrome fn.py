def is_palindrome(text):
    """Check if the given text is a palindrome.
    
    A palindrome is a string that reads the same forwards and backwards,
    ignoring case, spaces, and punctuation.
    
    Args:
        text (str): The string to check.
        
    Returns:
        bool: True if the text is a palindrome, False otherwise.
        
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Edge case: empty string or single character
    if len(cleaned_text) <= 1:
        return True
    
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]

def run_tests():
    """Run test cases for the palindrome function."""
    # List of test cases: (input, expected_result)
    test_cases = [
        ("", True),                     # Empty string
        ("a", True),                    # Single character
        ("race a car", False),          # Non-palindrome
        ("A man a plan a canal Panama", True),  # Classic palindrome with spaces
        ("Was it a car or a cat I saw", True),  # Longer palindrome
        ("hello", False),               # Simple non-palindrome
        ("12321", True),               # Numeric palindrome
        ("A Santa at NASA", True),      # Palindrome with mixed case
        ("!@#$%", True),               # Only special characters (becomes empty when cleaned)
    ]
    
    print("Running palindrome tests...")
    print("-" * 40)
    
    for text, expected in test_cases:
        result = is_palindrome(text)
        status = "✓" if result == expected else "✗"
        print(f'Testing "{text}":')
        print(f"Expected: {expected}, Got: {result} {status}")
        print()
    
    # Test error case
    print("Testing error cases...")
    try:
        is_palindrome(123)  # Should raise TypeError
        print("TypeError test: ✗")
    except TypeError:
        print("TypeError test: ✓")

if __name__ == "__main__":
    run_tests()
