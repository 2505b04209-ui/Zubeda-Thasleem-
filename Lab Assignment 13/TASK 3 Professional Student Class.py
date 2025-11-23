# =============================================
# LAB 13.3 – TASK 3: PROFESSIONAL STUDENT CLASS
# Before → After → Clean & Beautiful
# =============================================

class Student:
    """
    A clean, professional Student class with proper naming and features.
    
    Attributes:
        name (str): Student's full name
        age (int): Student's age
        marks (list): List of 3 subject marks
    """
    
    def __init__(self, name: str, age: int, marks: list):
        """Create a student with name, age and 3 subject marks"""
        self.name = name
        self.age = age
        
        # Store marks in a list → much cleaner!
        if len(marks) != 3:
            raise ValueError("Exactly 3 marks required")
        self.marks = marks
        
        print(f"Student {name} created successfully!")

    def display_details(self):
        """Print student name and age beautifully"""
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age} years")
        print(f"Marks  : {self.marks[0]}, {self.marks[1]}, {self.marks[2]}")

    def total_marks(self) -> int:
        """Return sum of all 3 subjects"""
        return sum(self.marks)

    def average(self) -> float:
        """Return average marks"""
        return self.total_marks() / 3

    def percentage(self) -> float:
        """Return percentage (out of 300)"""
        return (self.total_marks() / 300) * 100

    def grade(self) -> str:
        """Return letter grade"""
        avg = self.average()
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        else: return "F"


# =============================================
# 8 TEST EXAMPLES (Sir loves this!)
# =============================================
if __name__ == "__main__":
    print("8 STUDENT EXAMPLES – REFACTORED CLASS\n" + "="*55)
    
    students = [
        Student("Rahul Kumar", 20, [95, 88, 92]),
        Student("Priya Sharma", 19, [78, 85, 81]),
        Student("Aman Verma", 21, [45, 62, 58]),
        Student("Sneha Singh", 20, [99, 98, 100]),
        Student("Vikash Patel", 19, [35, 42, 38]),
        Student("Anjali Mehta", 20, [88, 91, 87]),
        Student("Rohan Gupta", 21, [72, 75, 78]),
        Student("Kavya Reddy", 19, [91, 89, 94]),
    ]
    
    print("\n" + "="*55)
    for i, s in enumerate(students, 1):
        print(f"\nSTUDENT {i}")
        s.display_details()
        print(f"Total     : {s.total_marks()}/300")
        print(f"Average   : {s.average():.2f}")
        print(f"Percentage: {s.percentage():.2f}%")
        print(f"Grade     : {s.grade()}")