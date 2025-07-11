"""
Example of a problematic addition that should trigger Copilot PR review feedback.
This file demonstrates common issues that Copilot should catch during PR reviews.
"""

# This function has multiple issues that Copilot should identify:
# 1. No type hints
# 2. Poor docstring
# 3. No error handling
# 4. Poor variable names

def mod(x, y):
    """Does modulo."""
    return x % y

def fact(n):
    """Factorial."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

class AdvancedCalculator:
    """Calculator with more operations."""
    
    def log(self, x, base):
        """Log function."""
        import math
        return math.log(x) / math.log(base)
    
    def sin(self, x):
        """Sin function."""
        import math
        return math.sin(x)
