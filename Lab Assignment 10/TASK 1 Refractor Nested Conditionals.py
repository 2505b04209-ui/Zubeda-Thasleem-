# =============================================
# LAB 10.3 – TASK 1: Refactor Nested Conditionals
# AI Tool: GROK (Your Smart Reviewer)
# Before → After → 8 Examples
# =============================================

# -------------------------------------------------
# ORIGINAL CODE (Nested & Messy)
# -------------------------------------------------
"""
def discount(price, category):
    if category == "student":
        if price > 1000:
            return price * 0.9
        else:
            return price * 0.95
    else:
        if price > 2000:
            return price * 0.85
        else:
            return price
"""

# -------------------------------------------------
# REFACTORED CODE (Clean + Dictionary)
# -------------------------------------------------
def discount(price, category):
    """
    Calculate discounted price based on category and amount.

    Rules:
        - Student: 10% off if >1000, else 5%
        - Others: 15% off if >2000, else no discount

    Args:
        price (float): Original price
        category (str): "student" or other

    Returns:
        float: Final price after discount

    Examples:
        See 8 test cases below
    """
    # Define discount rules using dictionary
    rules = {
        "student": {1000: 0.10, 0: 0.05},  # >1000: 10%, else: 5%
        "other":   {2000: 0.15, 0: 0.00}   # >2000: 15%, else: 0%
    }
    
    # Normalize category
    cat = "student" if category.lower() == "student" else "other"
    
    # Get threshold and discount rate
    thresholds = rules[cat]
    discount_rate = next(
        (rate for threshold, rate in thresholds.items() if price > threshold),
        thresholds[0]  # default (lowest threshold)
    )
    
    # Apply discount
    return price * (1 - discount_rate)


# =============================================
# TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – DISCOUNT CALCULATOR\n" + "="*50)
    
    tests = [
        (1200, "student", 1080.0),   # >1000 → 10%
        (800,  "student", 760.0),    # ≤1000 → 5%
        (2500, "staff",   2125.0),   # >2000 → 15%
        (1500, "other",   1500.0),   # ≤2000 → 0%
        (1000, "Student", 950.0),    # case-insensitive
        (2000, "other",   2000.0),   # edge: =2000 → no discount
        (0,    "student", 0.0),      # zero price
        (5000, "VIP",     4250.0),   # falls to "other"
    ]

    for i, (price, cat, expected) in enumerate(tests, 1):
        result = discount(price, cat)
        status = "PASS" if abs(result - expected) < 0.01 else "FAIL"
        print(f"{i}. Input: price={price}, category='{cat}'")
        print(f"    Output: {result:.2f} | Expected: {expected} → {status}\n")