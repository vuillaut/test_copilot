# Test Copilot

A simple Python calculator project to test GitHub Copilot's online capabilities and PR review features.

## Project Structure

- `calculator.py` - Main calculator module with basic arithmetic operations
- `test_calculator.py` - Unit tests for the calculator
- `requirements.txt` - Python dependencies
- `.github/copilot-instructions.md` - GitHub Copilot instructions for PR reviews

## Usage

```python
from calculator import Calculator

calc = Calculator()
result = calc.add(2, 3)  # Returns 5
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the calculator demo:
```bash
python calculator.py
```

## Running Tests

Run all tests:
```bash
python -m pytest test_calculator.py -v
```

Run tests with coverage:
```bash
python -m pytest test_calculator.py -v --cov=calculator --cov-report=term-missing
```

## Testing GitHub Copilot PR Reviews

This repository is specifically designed to test GitHub Copilot's PR review capabilities. Here are some scenarios to try:

### 🔍 **Test Scenarios for PR Reviews**

1. **Missing Type Hints**: Create a PR that adds new functions without type hints
2. **Missing Tests**: Add new functionality without corresponding unit tests
3. **Poor Documentation**: Add methods without proper docstrings
4. **Error Handling**: Introduce functions that don't handle edge cases
5. **Style Issues**: Submit code that doesn't follow PEP 8 guidelines

### 📋 **What Copilot Should Catch**

Based on the instructions in `.github/copilot-instructions.md`, Copilot should:
- Request type hints for function parameters and return types
- Ask for comprehensive docstrings with Args/Returns/Raises sections
- Flag missing error handling (especially division by zero)
- Suggest additional test cases for edge conditions
- Point out PEP 8 style violations
- Recommend security best practices

### 🚀 **Quick Test Ideas**

Try adding these features in separate PRs to test Copilot:
- Modulo operation (`%`)
- Factorial function
- Logarithm operations
- Trigonometric functions
- Memory functions (store/recall)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.