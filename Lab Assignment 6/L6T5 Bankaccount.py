# =============================================
# TASK 5: BANK ACCOUNT SIMULATION
# Prompt: "# Task 5: Bank account with deposit, withdraw, check balance"
# AI Tool: GitHub Copilot (VS Code)
# =============================================

class BankAccount:
    """
    BankAccount class simulates a real bank account.
    Features:
        - Deposit (positive amount only)
        - Withdraw (valid amount <= balance)
        - Check balance
    Uses:
        - Classes (OOP)
        - Conditionals (if/elif/else)
        - Loops (in test)
    """

    # Step 1: Constructor – Initialize balance
    def __init__(self, initial_balance=0):
        """
        Create account with starting balance.
        Args:
            initial_balance (float): Default 0
        """
        self.balance = initial_balance
        print(f"Account created. Initial balance: ₹{self.balance:.2f}")

    # Step 2: Deposit money
    def deposit(self, amount):
        """
        Add money to account.
        Condition: amount > 0
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount:.2f}")
        else:
            print("Error: Deposit amount must be positive!")

    # Step 3: Withdraw money
    def withdraw(self, amount):
        """
        Remove money from account.
        Conditions:
            1. amount > 0
            2. amount <= balance
        """
        if amount <= 0:
            print("Error: Withdraw amount must be positive!")
        elif amount > self.balance:
            print(f"Insufficient funds! Available: ₹{self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew: ₹{amount:.2f}")

    # Step 4: Check current balance
    def check_balance(self):
        """
        Return current balance.
        No condition needed – just read.
        """
        print(f"Current Balance: ₹{self.balance:.2f}")
        return self.balance


# =============================================
# MULTIPLE TEST EXAMPLES (With Loop for Transactions)
# =============================================
print("\n" + "="*55)
print("TASK 5: BANK ACCOUNT SIMULATION – FULL TEST")
print("="*55)

# Example 1: Create account with ₹100
acc = BankAccount(100)

# Example 2: Deposit money
acc.deposit(50)
acc.deposit(-20)  # Invalid

# Example 3: Withdraw valid/invalid amounts
acc.withdraw(30)
acc.withdraw(200)  # Insufficient

# Example 4: Final balance
acc.check_balance()

# Example 5: Loop through transactions
print("\n--- Transaction History (Loop Test) ---")
transactions = [25, -10, 40, 15, 100]  # Mixed valid/invalid
for amt in transactions:
    if amt > 0:
        acc.deposit(amt)
    else:
        acc.withdraw(-amt)  # Try to withdraw negative (invalid)

# Final balance after loop
acc.check_balance()