# =============================================
# LAB 10.3 – TASK 5: Code Review on Error Handling
# AI Tool | Before → After → 8 Examples
# =============================================
# -------------------------------------------------
# ORIGINAL CODE (Dangerous )
# -------------------------------------------------
"""
def div(a,b):
    return a/b
print(div(10,0))
"""
# This crashes with ZeroDivisionError!

# -------------------------------------------------
# IMPROVED & SAFE CODE (Full Size + Comments)
# -------------------------------------------------

def divide_numbers(numerator, denominator):
    """
    Safely divide two numbers with full error handling.

    This function performs division while protecting against:
    - Division by zero
    - Invalid input types (non-numeric)
    - Edge cases (float, large numbers)

    Args:
        numerator (int/float): The number to be divided (dividend)
        denominator (int/float): The number to divide by (divisor)

    Returns:
        float: Result of division, rounded to 2 decimal places
               Returns None if error occurs

    Raises:
        ZeroDivisionError: If denominator is zero
        TypeError: If inputs are not numbers
    """
    
    # ------------------------------------------------------------------
    # STEP 1: Input Validation – Check if both inputs are numbers
    # ------------------------------------------------------------------
    if not isinstance(numerator, (int, float)):
        print("Error: Numerator must be a number (int or float)")
        return None
    
    if not isinstance(denominator, (int, float)):
        print("Error: Denominator must be a number (int or float)")
        return None

    # ------------------------------------------------------------------
    # STEP 2: Check for Division by Zero
    # ------------------------------------------------------------------
    if denominator == 0:
        print("Critical Error: Cannot divide by zero!")
        print("   → Mathematical rule: x / 0 is undefined")
        return None

    # ------------------------------------------------------------------
    # STEP 3: Perform Safe Division
    # ------------------------------------------------------------------
    try:
        # Perform the actual division
        result = numerator / denominator
        
        # Round to 2 decimal places for clean output
        result_rounded = round(result, 2)
        
        # Success message
        print(f"Division successful: {numerator} ÷ {denominator} = {result_rounded}")
        
        # Return the clean result
        return result_rounded

    except Exception as e:
        # Catch any unexpected error (shouldn't happen, but safe)
        print(f"Unexpected error during division: {e}")
        return None


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – SAFE DIVISION WITH ERROR HANDLING\n" + "="*70)
    
    # List of test cases: (numerator, denominator, expected)
    test_cases = [
        (10, 2, 5.0),           # Normal division
        (15, 3, 5.0),           # Same result
        (7, 2, 3.5),            # Float result
        (10, 0, None),          # Divide by zero
        (-8, 2, -4.0),          # Negative numerator
        (8, -2, -4.0),          # Negative denominator
        (0, 5, 0.0),            # Zero numerator
        ("10", 2, None),        # String input (invalid)
    ]

    for i, (num, den, expected) in enumerate(test_cases, 1):
        print(f"\n{i}. TEST CASE: {num} ÷ {den}")
        print("-" * 50)
        
        # Call the safe function
        result = divide_numbers(num, den)
        
        # Compare with expected
        if result == expected:
            status = "PASS"
        else:
            status = "FAIL"
        
        print(f"   → Result: {result} | Expected: {expected} → {status}")
        print("-" * 50)