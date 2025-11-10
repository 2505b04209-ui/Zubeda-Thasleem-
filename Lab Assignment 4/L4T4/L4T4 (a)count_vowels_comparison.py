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
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert text to lowercase to count both upper and lower case vowels
    text = text.lower()
    
    # Define vowels
    vowels = 'aeiou'
    
    # Initialize counter
    count = 0
    
    # Count each vowel in the text
    for char in text:
        if char in vowels:
            count += 1
    
    return count

# Example usage
if __name__ == "__main__":
    # Test with a sample text
    sample_text = "Hello World"
    result = count_vowels(sample_text)
    print(f"Number of vowels in '{sample_text}': {result}")
