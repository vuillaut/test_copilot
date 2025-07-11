"""
Comprehensive test suite for the ScientificCalculator class.
Demonstrates proper testing practices with edge cases and error handling.
"""

import math
import pytest
from examples.good_code_example import ScientificCalculator

class TestScientificCalculator:
    """Test cases for the ScientificCalculator class."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = ScientificCalculator()
    
    # Modulo operation tests
    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        assert self.calc.modulo(10, 3) == 1
        assert self.calc.modulo(15, 4) == 3
        assert self.calc.modulo(8, 2) == 0
    
    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        assert self.calc.modulo(-10, 3) == 2  # Python's modulo behavior
        assert self.calc.modulo(10, -3) == -2
    
    def test_modulo_zero_divisor(self):
        """Test that modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate modulo with zero divisor"):
            self.calc.modulo(10, 0)
    
    def test_modulo_invalid_types(self):
        """Test that modulo with invalid types raises TypeError."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            self.calc.modulo("10", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            self.calc.modulo(10, "3")
    
    # Factorial tests
    def test_factorial_small_numbers(self):
        """Test factorial of small positive numbers."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(6) == 720
    
    def test_factorial_negative_number(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate factorial of negative number"):
            self.calc.factorial(-1)
    
    def test_factorial_non_integer(self):
        """Test that factorial of non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Factorial requires an integer input"):
            self.calc.factorial(5.5)
        with pytest.raises(TypeError, match="Factorial requires an integer input"):
            self.calc.factorial("5")
    
    # Logarithm tests
    def test_logarithm_natural_log(self):
        """Test natural logarithm (base e)."""
        assert abs(self.calc.logarithm(math.e) - 1.0) < 1e-10
        assert abs(self.calc.logarithm(1) - 0.0) < 1e-10
        assert self.calc.logarithm(math.e ** 2) == pytest.approx(2.0)
    
    def test_logarithm_base_10(self):
        """Test logarithm with base 10."""
        assert self.calc.logarithm(10, 10) == pytest.approx(1.0)
        assert self.calc.logarithm(100, 10) == pytest.approx(2.0)
        assert self.calc.logarithm(1000, 10) == pytest.approx(3.0)
    
    def test_logarithm_base_2(self):
        """Test logarithm with base 2."""
        assert self.calc.logarithm(2, 2) == pytest.approx(1.0)
        assert self.calc.logarithm(8, 2) == pytest.approx(3.0)
        assert self.calc.logarithm(16, 2) == pytest.approx(4.0)
    
    def test_logarithm_invalid_value(self):
        """Test that logarithm of non-positive number raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm requires a positive value"):
            self.calc.logarithm(0)
        with pytest.raises(ValueError, match="Logarithm requires a positive value"):
            self.calc.logarithm(-5)
    
    def test_logarithm_invalid_base(self):
        """Test that logarithm with invalid base raises ValueError."""
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            self.calc.logarithm(10, 0)
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            self.calc.logarithm(10, -2)
        with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
            self.calc.logarithm(10, 1)
    
    def test_logarithm_invalid_types(self):
        """Test that logarithm with invalid types raises TypeError."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            self.calc.logarithm("10", 2)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            self.calc.logarithm(10, "2")
    
    # Sine function tests
    def test_sine_known_values(self):
        """Test sine function with known values."""
        assert self.calc.sine(0) == pytest.approx(0.0)
        assert self.calc.sine(math.pi / 2) == pytest.approx(1.0)
        assert self.calc.sine(math.pi) == pytest.approx(0.0, abs=1e-10)
        assert self.calc.sine(3 * math.pi / 2) == pytest.approx(-1.0)
    
    def test_sine_negative_angles(self):
        """Test sine function with negative angles."""
        assert self.calc.sine(-math.pi / 2) == pytest.approx(-1.0)
        assert self.calc.sine(-math.pi) == pytest.approx(0.0, abs=1e-10)
    
    def test_sine_invalid_type(self):
        """Test that sine with invalid type raises TypeError."""
        with pytest.raises(TypeError, match="Angle must be a number"):
            self.calc.sine("90")
        with pytest.raises(TypeError, match="Angle must be a number"):
            self.calc.sine(None)
