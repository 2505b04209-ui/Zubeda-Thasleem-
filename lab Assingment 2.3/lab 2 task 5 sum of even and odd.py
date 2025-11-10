# Program to calculate sum of even and odd numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension and sum() for better readability and efficiency
even_sum = sum(num for num in numbers if num % 2 == 0)
odd_sum = sum(num for num in numbers if num % 2 != 0)

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
