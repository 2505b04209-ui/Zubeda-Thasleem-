# =============================================
# TASK 3: RUNTIME ERROR – Division by Zero
# =============================================
# Prompt: "Fix division by zero: print(10 / 0)"

def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            return "Cannot divide by zero"
        return numerator / denominator
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Test the function
print("Task 3 Output:", safe_divide(10, 0))  # Safe case
print("Task 3 Output:", safe_divide(10, 2))  # Normal division