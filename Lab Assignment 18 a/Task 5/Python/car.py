"""
Task 5: Python Car Class - Final Version with Comments
"""
class Car:
    def __init__(self, brand, model, year):
        """Initialize Car object with brand, model, and year attributes"""
        self.brand = brand      # Car manufacturer
        self.model = model      # Car model name
        self.year = year        # Manufacturing year (integer)

    def display_details(self):
        """Display formatted car details"""
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

if __name__ == "__main__":
    # Create and test object
    toyota = Car("Toyota", "Corolla", 2020)
    toyota.display_details()
