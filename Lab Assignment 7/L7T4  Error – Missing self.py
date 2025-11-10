
# =============================================
# TASK 4: CLASS ERROR – Missing 'self'
# =============================================
# Prompt: "Fix class: def __init__(name): self.name = name"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)

        print("Age:", self.age)

# Create an instance
print("Task 4 Output:")
person = Person("John", 30)
person.display()
