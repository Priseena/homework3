"""
This module contains basic arithmetic operations using the Decimal type.
"""

from decimal import Decimal

# Define the functions with type hints
def add(a: Decimal, b: Decimal) -> Decimal:
    """Return the sum of two Decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Return the difference between two Decimal numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Return the product of two Decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Return the quotient of two Decimal numbers. Raise a ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
