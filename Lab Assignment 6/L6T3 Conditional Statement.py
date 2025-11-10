# =============================================
# TASK 3: CONDITIONAL STATEMENTS – Age Classification
# Prompt: "Write function to classify age using if-elif-else and match-case"
# AI Tool: GitHub Copilot (VS Code)
# =============================================

def classify_age(age):
    """
    Classify person based on age using if-elif-else.
    
    Args:
        age (int): Age in years (0 or positive)
    
    Returns:
        str: "Child", "Teen", or "Adult"
    
    Logic:
        - Child: 0–12
        - Teen: 13–19
        - Adult: 20+
    
    Why order matters?
        → 16 would match both <13 and <=19 → so check <13 FIRST!
    """
    # Step 1: Input validation
    if not isinstance(age, int) or age < 0:
        print("Error: Age must be a non-negative integer!")
        return "Invalid"

    # Step 2: if-elif-else chain
    if age < 13:                    # Child: 0 to 12
        return "Child"
    elif age <= 19:                 # Teen: 13 to 19
        return "Teen"
    else:                           # Adult: 20 and above
        return "Adult"


def classify_age_match(age):
    """
    Classify person using match-case (Python 3.10+).
    
    Why match-case?
        → Cleaner, modern syntax
        → Same logic, different style
    """
    # Step 1: Input validation
    if not isinstance(age, int) or age < 0:
        print("Error: Age must be a non-negative integer!")
        return "Invalid"

    # Step 2: match-case with guard clauses
    match age:
        case age if age < 13:       # Guard: age < 13
            return "Child"
        case age if age <= 19:      # Guard: age <= 19
            return "Teen"
        case _:                     # Default case
            return "Adult"


# =============================================
# MULTIPLE TEST EXAMPLES (Including Edge Cases)
# =============================================
print("\n" + "="*65)
print("TASK 3: AGE CLASSIFICATION – if-elif-else vs match-case")
print("="*65)

# Example 1: Normal cases
print("1. NORMAL CASES")
print(f"  Age 10 → if-elif:  {classify_age(10)}")        # Child
print(f"  Age 10 → match:    {classify_age_match(10)}")   # Child

print(f"  Age 16 → if-elif:  {classify_age(16)}")        # Teen
print(f"  Age 16 → match:    {classify_age_match(16)}")   # Teen

print(f"  Age 25 → if-elif:  {classify_age(25)}")        # Adult
print(f"  Age 25 → match:    {classify_age_match(25)}")   # Adult

# Example 2: Edge cases
print("\n2. EDGE CASES")
print(f"  Age 12 → Child? {classify_age(12)}")           # Child
print(f"  Age 13 → Teen?  {classify_age(13)}")           # Teen
print(f"  Age 19 → Teen?  {classify_age(19)}")           # Teen
print(f"  Age 20 → Adult? {classify_age(20)}")           # Adult

# Example 3: Invalid inputs
print("\n3. INVALID INPUTS")
print(f"  Age -5 → {classify_age(-5)}")                  # Invalid
print(f"  Age 3.5 → {classify_age(3.5)}")                # Invalid (not int)

# Example 4: Large age
print("\n4. LARGE AGE")
print(f"  Age 100 → {classify_age(100)}")                # Adult
print(f"  Age 100 → match: {classify_age_match(100)}")  # Adult