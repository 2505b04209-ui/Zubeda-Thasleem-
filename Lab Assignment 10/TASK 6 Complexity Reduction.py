# =============================================
# LAB 10.3 – TASK 6: Complexity Reduction
# AI Tool: GROK | Before → After → 8 Examples
# =============================================

# -------------------------------------------------
# ORIGINAL CODE (Deeply Nested – Sir Gave)
# -------------------------------------------------
"""
def grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            if score >= 70:
                return "C"
            else:
                if score >= 60:
                    return "D"
                else:
                    return "F"
"""

# -------------------------------------------------
# REDUCED & CLEAN CODE (Full Size + Comments)
# -------------------------------------------------
def assign_grade(score):
    """
    Assign letter grade based on score using clean elif chain.

    Grading Scale:
        90–100 → A
        80–89  → B
        70–79  → C
        60–69  → D
        <60    → F

    Args:
        score (int/float): Student score

    Returns:
        str: Letter grade (A/B/C/D/F)
             Returns "Invalid" if score <0 or >100

    Examples:
        95 → "A", 82 → "B", 55 → "F", -5 → "Invalid"
    """
    
    # ------------------------------------------------------------------
    # STEP 1: Input Validation – Score must be number
    # ------------------------------------------------------------------
    if not isinstance(score, (int, float)):
        print("Error: Score must be a number (int or float)")
        return "Invalid"

    # ------------------------------------------------------------------
    # STEP 2: Range Validation – Score between 0 and 100
    # ------------------------------------------------------------------
    if score < 0:
        print("Error: Score cannot be negative")
        return "Invalid"
    
    if score > 100:
        print("Error: Score cannot exceed 100")
        return "Invalid"

    # ------------------------------------------------------------------
    # STEP 3: Grade Assignment using elif (Clean Flow)
    # ------------------------------------------------------------------
    if score >= 90:
        # Top tier performance
        print(f"Score {score}: Excellent! → Grade A")
        return "A"
    
    elif score >= 80:
        # Good performance
        print(f"Score {score}: Good job! → Grade B")
        return "B"
    
    elif score >= 70:
        # Average performance
        print(f"Score {score}: Fair → Grade C")
        return "C"
    
    elif score >= 60:
        # Passing
        print(f"Score {score}: Just passed → Grade D")
        return "D"
    
    else:
        # Below passing
        print(f"Score {score}: Needs improvement → Grade F")
        return "F"


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – GRADE ASSIGNMENT SYSTEM\n" + "="*70)
    
    # Test cases: (score, expected_grade)
    test_cases = [
        (95, "A"),           # Top of A
        (82, "B"),           # Middle B
        (75, "C"),           # Middle C
        (60, "D"),           # Edge D
        (59, "F"),           # Just below D
        (100, "A"),          # Max score
        (-5, "Invalid"),     # Negative
        (105, "Invalid"),    # Over 100
    ]

    for i, (score, expected) in enumerate(test_cases, 1):
        print(f"\n{i}. INPUT SCORE: {score}")
        print("-" * 50)
        
        # Call the function
        result = assign_grade(score)
        
        # Check result
        status = "PASS" if result == expected else "FAIL"
        
        print(f"   → Grade: {result} | Expected: {expected} → {status}")
        print("-" * 50)