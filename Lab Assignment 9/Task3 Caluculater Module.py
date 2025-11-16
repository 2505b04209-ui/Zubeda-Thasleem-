# =============================================
# LAB 9.3 – TASK 3: Calculator Module
# Objective: Module + Function Docstrings (NumPy Style)
# 8 EXAMPLES + FULL EXPLANATION
# AI Tool: GROK
# =============================================

"""
Calculator Module
================

A simple arithmetic calculator with four basic operations.

This module provides functions for addition, subtraction, multiplication,
and division. All functions accept numeric inputs and return float results.
Division handles zero division by returning 0.0.

Functions
---------
add(a, b)
    Return a + b
subtract(a, b)
    Return a - b
multiply(a, b)
    Return a * b
divide(a, b)
    Return a / b (0 if b == 0)

Examples
--------
>>> add(5, 3)
8.0
>>> divide(10, 0)
0.0
"""

# -------------------------------------------------
# MANUAL: Function Docstrings (NumPy Style)
# -------------------------------------------------
def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        First number
    b : int or float
        Second number

    Returns
    -------
    float
        Sum of a and b

    Examples
    --------
    >>> add(5, 3)
    8.0
    >>> add(-1, 1)
    0.0
    """
    return float(a + b)


def subtract(a, b):
    """
    Subtract b from a.

    Parameters
    ----------
    a : int or float
        Minuend
    b : int or float
        Subtrahend

    Returns
    -------
    float
        a - b

    Examples
    --------
    >>> subtract(10, 4)
    6.0
    """
    return float(a - b)


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First factor
    b : int or float
        Second factor

    Returns
    -------
    float
        Product of a and b

    Examples
    --------
    >>> multiply(3, 4)
    12.0
    """
    return float(a * b)


def divide(a, b):
    """
    Divide a by b.

    If b is 0, returns 0.0 to avoid ZeroDivisionError.

    Parameters
    ----------
    a : int or float
        Dividend
    b : int or float
        Divisor (non-zero)

    Returns
    -------
    float
        a / b or 0.0 if b == 0

    Examples
    --------
    >>> divide(10, 2)
    5.0
    >>> divide(5, 0)
    0.0
    """
    return float(a / b) if b != 0 else 0.0


# =============================================
# AI-GENERATED MODULE DOCSTRING (By GROK)
# =============================================
"""
Arithmetic calculator module.

Provides:
- add: a + b
- subtract: a - b
- multiply: a * b
- divide: a / b (safe)

All return float. Division by zero returns 0.
"""


# =============================================
# 8 TEST EXAMPLES (Run to see output)
# =============================================
if __name__ == "__main__":
    print("8 EXAMPLES – CALCULATOR MODULE\n" + "="*50)

    print("1. Addition:")
    print(f"   add(5, 3) = {add(5, 3)}")
    print(f"   add(-1, 1) = {add(-1, 1)}\n")

    print("2. Subtraction:")
    print(f"   subtract(10, 4) = {subtract(10, 4)}")
    print(f"   subtract(0, 5) = {subtract(0, 5)}\n")

    print("3. Multiplication:")
    print(f"   multiply(3, 4) = {multiply(3, 4)}")
    print(f"   multiply(0, 100) = {multiply(0, 100)}\n")

    print("4. Division:")
    print(f"   divide(10, 2) = {divide(10, 2)}")
    print(f"   divide(5, 0) = {divide(5, 0)}\n")

    print("5. Mixed Operations:")
    print(f"   add(multiply(2, 3), subtract(10, 4)) = {add(multiply(2, 3), subtract(10, 4))}\n")

    print("6. Large Numbers:")
    print(f"   multiply(1000, 1000) = {multiply(1000, 1000)}\n")

    print("7. Floating Point:")
    print(f"   divide(1, 3) = {divide(1, 3):.2f}\n")

    print("8. Zero Division Safety:")
    print(f"   divide(100, 0) = {divide(100, 0)}")