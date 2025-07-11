# GitHub Copilot Instructions for PR Reviews

## Project Overview
This is a simple Python calculator project designed to test GitHub Copilot's capabilities. The project follows Python best practices and includes comprehensive testing.

## Code Review Guidelines

### General Principles
- Ensure code follows PEP 8 Python style guidelines
- Verify that all functions have proper docstrings
- Check for appropriate error handling and edge cases
- Validate that unit tests cover new functionality
- Ensure backward compatibility is maintained

### Specific Focus Areas

#### Code Quality
- **Type Safety**: Suggest type hints for function parameters and return types
- **Documentation**: Verify all public methods have clear docstrings with parameter descriptions
- **Error Handling**: Check for appropriate exception handling, especially for division by zero and invalid inputs
- **Performance**: Look for opportunities to optimize calculations or memory usage

#### Testing Requirements
- **Coverage**: New features must include corresponding unit tests
- **Edge Cases**: Tests should cover boundary conditions (zero, negative numbers, large numbers)
- **Error Scenarios**: Verify that error conditions are properly tested with pytest.raises
- **Test Naming**: Test method names should clearly describe what is being tested

#### Security Considerations
- **Input Validation**: Ensure all user inputs are properly validated
- **Error Messages**: Verify error messages don't expose sensitive information
- **Dependencies**: Check that any new dependencies are secure and necessary

### Mathematical Accuracy
- **Precision**: Be aware of floating-point precision issues in calculations
- **Domain Validation**: Ensure mathematical operations are valid for their inputs (e.g., no negative square roots)
- **Range Checking**: Consider overflow/underflow for very large or small numbers

### Python-Specific Guidelines
- **Imports**: Verify imports are organized and unused imports are removed
- **Code Style**: Enforce consistent indentation, naming conventions, and line length
- **Best Practices**: Suggest more Pythonic approaches when applicable
- **Resource Management**: Check for proper resource cleanup if applicable

### Review Comments Style
- Be constructive and educational in feedback
- Provide specific examples when suggesting improvements
- Reference relevant Python documentation or PEP standards
- Suggest specific test cases for edge conditions
- Highlight both strengths and areas for improvement

### Automated Checks to Verify
- All tests pass with `python -m pytest`
- Code follows PEP 8 standards
- No unused imports or variables
- Proper exception handling for error conditions

### Examples of Good Practices to Encourage
```python
def divide(self, a: float, b: float) -> float:
    """
    Divide a by b and return the result.
    
    Args:
        a (float): The dividend
        b (float): The divisor
        
    Returns:
        float: The result of a/b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Red Flags to Watch For
- Missing or inadequate tests for new functionality
- Functions without docstrings
- Hardcoded values that should be configurable
- Missing error handling for obvious failure modes
- Complex functions that could be broken down
- Inconsistent coding style within the same file

## Additional Notes
- Encourage contributors to run tests locally before submitting PRs
- Suggest using type checkers like mypy for additional safety
- Remind about the importance of maintaining the simple, educational nature of this project
