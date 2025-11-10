"""
================================================================================
LAB 7.3 – AI ERROR DEBUGGING
================================================================================
Course     : 24CS002PC215 – AI Assisted Coding
Assignment : 7.3 / 24
Name       : ____________________
Roll No    : ____________________
================================================================================
"""

# =============================================
# TASK 1: SYNTAX ERROR – Missing Colon
# =============================================
# Prompt: "Fix this syntax error: def add(a, b) print(a + b)"
def add(a, b):  # Added missing colon
    print(a + b)  # Added proper indentation
print("Task 1 Output:", add(5, 3))

