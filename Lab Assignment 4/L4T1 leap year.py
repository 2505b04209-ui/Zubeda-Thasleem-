def is_leap_year(year):
    """
    Determine whether a given year is a leap year.
    
    Args:
        year (int): The year to check (must be a positive integer)
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    Raises:
        ValueError: If the year is not a positive integer
    """
    # Input validation
    if not isinstance(year, int) or year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Rule 1: If year is divisible by 400, it's a leap year
    if year % 400 == 0:
        return True
    
    # Rule 2: If year is divisible by 100 but not 400, it's NOT a leap year
    if year % 100 == 0:
        return False
    
    # Rule 3: If year is divisible by 4 (and not caught by above rules), it's a leap year
    return year % 4 == 0

# Test cases with explanations
def test_leap_years():
    """Run test cases for different years with explanations."""
    
    # Test Case 1: Year 2000
    print(f"Year 2000: {is_leap_year(2000)}")
    print("Explanation: 2000 is a leap year because it's divisible by 400")
    print()
    
    # Test Case 2: Year 1900
    print(f"Year 1900: {is_leap_year(1900)}")
    print("Explanation: 1900 is NOT a leap year because it's divisible by 100 but not by 400")
    print()
    
    # Test Case 3: Year 2024
    print(f"Year 2024: {is_leap_year(2024)}")
    print("Explanation: 2024 is a leap year because it's divisible by 4 and not by 100")
    print()
    
    # Test Case 4: Year 2019
    print(f"Year 2019: {is_leap_year(2019)}")
    print("Explanation: 2019 is NOT a leap year because it's not divisible by 4")
    print()

# Run the test cases
if __name__ == "__main__":
    print("=== Leap Year Checker Test Cases ===")
    print("-" * 35)
    test_leap_years()
