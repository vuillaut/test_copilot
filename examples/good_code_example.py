"""
Example of well-written code that follows all the guidelines in copilot-instructions.md.
This demonstrates the quality standards expected for this project.
"""

import math
from typing import Union

class ScientificCalculator:
    """
    A scientific calculator with advanced mathematical operations.
    
    This class extends basic arithmetic with logarithmic, trigonometric,
    and other mathematical functions following proper coding standards.
    """
    
    def modulo(self, dividend: Union[int, float], divisor: Union[int, float]) -> Union[int, float]:
        """
        Calculate the remainder when dividend is divided by divisor.
        
        Args:
            dividend (Union[int, float]): The number to be divided
            divisor (Union[int, float]): The number to divide by
            
        Returns:
            Union[int, float]: The remainder of dividend / divisor
            
        Raises:
            ValueError: If divisor is zero
            TypeError: If inputs are not numbers
        """
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        if divisor == 0:
            raise ValueError("Cannot calculate modulo with zero divisor")
        
        return dividend % divisor
    
    def factorial(self, number: int) -> int:
        """
        Calculate the factorial of a non-negative integer.
        
        Args:
            number (int): A non-negative integer
            
        Returns:
            int: The factorial of the input number
            
        Raises:
            ValueError: If number is negative
            TypeError: If number is not an integer
        """
        if not isinstance(number, int):
            raise TypeError("Factorial requires an integer input")
        
        if number < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        
        if number == 0 or number == 1:
            return 1
        
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result
    
    def logarithm(self, value: float, base: float = math.e) -> float:
        """
        Calculate the logarithm of a value with specified base.
        
        Args:
            value (float): The number to calculate logarithm for (must be positive)
            base (float, optional): The logarithm base. Defaults to e (natural log)
            
        Returns:
            float: The logarithm of value with the specified base
            
        Raises:
            ValueError: If value <= 0 or base <= 0 or base == 1
            TypeError: If inputs are not numbers
        """
        if not isinstance(value, (int, float)) or not isinstance(base, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        if value <= 0:
            raise ValueError("Logarithm requires a positive value")
        
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        
        return math.log(value) / math.log(base)
    
    def sine(self, angle_radians: float) -> float:
        """
        Calculate the sine of an angle in radians.
        
        Args:
            angle_radians (float): The angle in radians
            
        Returns:
            float: The sine of the angle
            
        Raises:
            TypeError: If angle is not a number
        """
        if not isinstance(angle_radians, (int, float)):
            raise TypeError("Angle must be a number")
        
        return math.sin(angle_radians)
