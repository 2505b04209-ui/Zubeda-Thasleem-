from car import Car

# Test 1: Attribute values are set correctly
car1 = Car("Toyota", "Corolla", 2020)
assert car1.brand == "Toyota"
assert car1.model == "Corolla"
assert car1.year == 2020

# Test 2: Different car object
car2 = Car("Honda", "Civic", 2018)
assert car2.brand == "Honda"
assert car2.model == "Civic"
assert car2.year == 2018

# Test 3: Year is an integer
car3 = Car("Ford", "Focus", 2015)
assert isinstance(car3.year, int)

print("All Python Car tests passed!")
