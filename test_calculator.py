"""
Unit tests for the calculator module.
"""

import pytest
from calculator import Calculator

class TestCalculator:
    """Test cases for the Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 15) == 25
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert self.calc.add(-2, -3) == -5
        assert self.calc.add(-5, 3) == -2
        assert self.calc.add(5, -3) == 2
    
    def test_add_zero(self):
        """Test addition with zero."""
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction operations."""
        assert self.calc.subtract(10, 3) == 7
        assert self.calc.subtract(5, 5) == 0
        assert self.calc.subtract(3, 10) == -7
    
    def test_multiply(self):
        """Test multiplication operations."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 10) == 0
        assert self.calc.multiply(2.5, 4) == 10.0
    
    def test_divide(self):
        """Test division operations."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(15, 3) == 5
        assert self.calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operations."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(10, 0) == 1
        assert self.calc.power(4, 0.5) == 2.0
    
    def test_square_root(self):
        """Test square root operations."""
        assert self.calc.square_root(16) == 4
        assert self.calc.square_root(25) == 5
        assert self.calc.square_root(0) == 0
        assert abs(self.calc.square_root(2) - 1.4142135623730951) < 1e-10
    
    def test_square_root_negative(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)
    
    def test_chaining_operations(self):
        """Test chaining multiple operations."""
        # (2 + 3) * 4 = 20
        result = self.calc.multiply(self.calc.add(2, 3), 4)
        assert result == 20
        
        # √(4^2) = 4
        result = self.calc.square_root(self.calc.power(4, 2))
        assert result == 4.0
