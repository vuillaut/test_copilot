"""
A simple calculator module for basic arithmetic operations.
"""

class Calculator:
    """A calculator class that performs basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent
    
    def square_root(self, number):
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5

def main():
    """Simple demonstration of the calculator."""
    calc = Calculator()
    
    print("Calculator Demo:")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"5 * 6 = {calc.multiply(5, 6)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2^3 = {calc.power(2, 3)}")
    print(f"√16 = {calc.square_root(16)}")

if __name__ == "__main__":
    main()
