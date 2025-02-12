"""
This module contains the Calculation class for basic arithmetic operations.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name, too-few-public-methods
class Calculation:
    """Class for performing basic arithmetic operations."""
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        """Return the result"""
        # Call the stored operation with a and b
        return self.operation(self.a, self.b)
    