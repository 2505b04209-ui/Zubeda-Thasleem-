# -------------------------------------------------------------------
# Task 2 - Bias Analysis: Checking if AI (or code logic) treats names fairly
# -------------------------------------------------------------------

# In this example, we simulate a "loan approval system".
# We'll give the system the same financial data for people with different names
# (male, female, and neutral names) to check if any bias exists.

# -------------------------------------------------------------------
# 1️⃣ Function for loan approval check
# -------------------------------------------------------------------
def loan_approval(name, income, debts):
    """
    Simple rule-based loan approval:
    - Approve if income > 30,000 and debts == 0
    - Reject otherwise
    """
    if income > 30000 and debts == 0:
        print(f"Loan approved for {name}")
    else:
        print(f"Loan rejected for {name}")


# -------------------------------------------------------------------
# 2️⃣ Test with multiple names (same income, same debt)
# -------------------------------------------------------------------
# Here we use 3 names — one male, one female, one neutral.
# All have exactly the same data.
# If results differ, that would show bias in the logic.

print("---- Testing Equal Profiles ----")
loan_approval("John", 50000, 0)    # male name
loan_approval("Mary", 50000, 0)    # female name
loan_approval("Alex", 50000, 0)    # gender-neutral name

# Expected output: All approved ✅ (No bias)
print()


# -------------------------------------------------------------------
# 3️⃣ Test with slightly different data (for comparison)
# -------------------------------------------------------------------
# Here we vary income and debts slightly to show how decisions change logically,
# not because of the name.

print("---- Testing Different Financial Conditions ----")
loan_approval("John", 25000, 0)    # low income, should be rejected
loan_approval("Mary", 40000, 1)    # has debt, should be rejected
loan_approval("Alex", 60000, 0)    # good income, should be approved
print()


# -------------------------------------------------------------------
# 4️⃣ Conclusion printout
# -------------------------------------------------------------------
print("Conclusion: All names treated equally for same conditions — No bias found.")

