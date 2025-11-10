def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Args:
        centimeters (float): Length in centimeters (must be non-negative)
    
    Returns:
        float: Length in inches, rounded to 3 decimal places
    
    Raises:
        ValueError: If the input is negative
        TypeError: If the input is not a number
    """
    # Input validation: check if input is a number (int or float)
    if not isinstance(centimeters, (int, float)):
        raise TypeError("Input must be a number")
    
    # Input validation: check if input is non-negative
    if centimeters < 0:
        raise ValueError("Input must be non-negative")
    
    # Conversion formula: 1 inch = 2.54 centimeters
    # Therefore, to convert cm to inches: divide by 2.54
    inches = centimeters / 2.54
    
    # Round to 3 decimal places for cleaner output
    return round(inches, 3)

# Test cases
def run_tests():
    """Run test cases with different measurements."""
    
    print("=== Centimeter to Inches Converter ===")
    print("-" * 35)
    
    # Test Case 1: 10 cm
    cm = 10
    inches = cm_to_inches(cm)
    print(f"{cm} centimeters = {inches} inches")
    
    # Test Case 2: 25.4 cm (exactly 10 inches)
    cm = 25.4
    inches = cm_to_inches(cm)
    print(f"{cm} centimeters = {inches} inches")
    
    # Test Case 3: 50 cm
    cm = 50
    inches = cm_to_inches(cm)
    print(f"{cm} centimeters = {inches} inches")
    
    # Test Case 4: 2.54 cm (exactly 1 inch)
    cm = 2.54
    inches = cm_to_inches(cm)
    print(f"{cm} centimeters = {inches} inches")
    
    # Test error cases
    try:
        cm_to_inches(-5)  # Should raise ValueError
    except ValueError as e:
        print("\nError test passed: Caught negative input")
    
    try:
        cm_to_inches("10")  # Should raise TypeError
    except TypeError as e:
        print("Error test passed: Caught non-numeric input")

# Run the test cases
if __name__ == "__main__":
    run_tests()