"""
================================================================================
LAB 6.3 – AI-BASED CODE COMPLETION
================================================================================
Course     : 24CS002PC215 – AI Assisted Coding
Assignment : 6.3 / 24
Week       : Week 3 – Wednesday
Name       : Zubeda Thasleem_
================================================================================
TASK 1 – CLASSES (Student) Use AI to complete Student class with attributes & method

================================================================================
"""
# =============================================
# TASK 1: Student Class with AI Completion
# Prompt: "# Task 1: Student class with name, age, grade, display method"
# AI Tool: GitHub Copilot (VS Code)
# =============================================

class Student:
    """
    Student class to store and display student information.
    Attributes:
        name (str): Name of the student
        age (int): Age in years
        grade (str): Grade like 'A', 'B+', etc.
    Methods:
        display_details(): Prints all info
    """
    
    # Step 1: Constructor – Runs when object is created
    def __init__(self, name, age, grade):
        """
        Initialize a new Student object.
        Args:
            name: str
            age: int
            grade: str
        """
        self.name = name      # Store name
        self.age = age        # Store age
        self.grade = grade    # Store grade
        print(f"New student created: {name}")

    # Step 2: Method to display details
    def display_details(self):
        """
        Print student info in formatted way.
        Uses f-strings for clean output.
        """
        print("\n--- Student Details ---")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age} years")
        print(f"Grade: {self.grade}")
        print("-----------------------")


# =============================================
# MULTIPLE TEST EXAMPLES
# =============================================
print("=== TASK 1: STUDENT CLASS TEST ===")

# Example 1: Alice
s1 = Student("Alice", 20, "A")
s1.display_details()

# Example 2: Bob
s2 = Student("Bob", 22, "B+")
s2.display_details()

# Example 3: Charlie (Failed student)
s3 = Student("Charlie", 19, "F")
s3.display_details()

# Example 4: Access attribute directly
print(f"Direct access → {s1.name} is {s1.age} years old")