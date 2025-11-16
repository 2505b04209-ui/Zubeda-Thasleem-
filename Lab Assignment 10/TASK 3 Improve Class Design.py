# =============================================
# LAB 10.3 – TASK 3: Improve Class Design
# AI Tool: GROK | Before → After → 8 Examples
# =============================================

# -------------------------------------------------
# ORIGINAL CODE (Poor Design – Sir Gave)
# -------------------------------------------------
"""
class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
    def pr(self):
        print("emp:",self.n,"salary:",self.s)
"""

# -------------------------------------------------
# IMPROVED CLASS (Clean OOP + Comments)
# -------------------------------------------------
class Employee:
    """
    Represents an employee with name and salary.

    Attributes:
        name (str): Full name of employee
        salary (float): Current salary in INR

    Methods:
        increase_salary(percentage): Add % increment
        display_info(): Print formatted details
    """
    
    # Constructor: Initialize employee with name and salary
    def __init__(self, name, salary):
        # Validate name is string and not empty
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        
        # Validate salary is positive number
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Salary must be a non-negative number")
        
        # Store name (strip whitespace)
        self.name = name.strip()
        
        # Store salary as float
        self.salary = float(salary)

    # Method: Increase salary by given percentage
    def increase_salary(self, percentage):
        """
        Increase salary by a percentage.

        Args:
            percentage (float): Increment % (e.g., 10 for 10%)

        Raises:
            ValueError: If percentage is negative
        """
        # Validate percentage is non-negative
        if percentage < 0:
            raise ValueError("Percentage cannot be negative")
        
        # Calculate increment amount
        increment = self.salary * (percentage / 100)
        
        # Update salary
        self.salary += increment
        
        # Print confirmation
        print(f"Salary increased by {percentage}% → +₹{increment:,.2f}")

    # Method: Display employee info in readable format
    def display_info(self):
        """
        Print employee name and current salary in formatted style.
        """
        # Print header
        print("=" * 40)
        print(f" EMPLOYEE DETAILS ")
        print("=" * 40)
        
        # Print name
        print(f"Name   : {self.name}")
        
        # Print salary with Indian formatting
        print(f"Salary : ₹{self.salary:,.2f}")
        print("=" * 40)


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – EMPLOYEE CLASS\n" + "="*60)
    
    # Example 1: Normal employee
    print("1. Normal Employee")
    e1 = Employee("Amit Sharma", 50000)
    e1.display_info()
    print()

    # Example 2: Salary increment
    print("2. 15% Increment")
    e2 = Employee("Priya Verma", 60000)
    e2.increase_salary(15)
    e2.display_info()
    print()

    # Example 3: Multiple increments
    print("3. Multiple Increments")
    e3 = Employee("Rohan Kumar", 40000)
    e3.increase_salary(10)
    e3.increase_salary(5)
    e3.display_info()
    print()

    # Example 4: Zero salary
    print("4. Zero Salary (Allowed)")
    e4 = Employee("Neha Gupta", 0)
    e4.display_info()
    print()

    # Example 5: Long name
    print("5. Long Name")
    e5 = Employee("Dr. Vikram Singh Choudhary", 120000)
    e5.display_info()
    print()

    # Example 6: Invalid name (Error)
    print("6. Invalid Name → Error")
    try:
        e6 = Employee("", 50000)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Example 7: Invalid salary (Error)
    print("7. Invalid Salary → Error")
    try:
        e7 = Employee("Test", -1000)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Example 8: Full profile with increment
    print("8. Full Profile + Increment")
    e8 = Employee("Arjun Reddy", 80000)
    e8.increase_salary(20)
    e8.display_info()