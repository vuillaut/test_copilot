# Contributing to Test Copilot

Thank you for your interest in contributing to this test project! This project is designed to test GitHub Copilot's online capabilities and PR review features.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests to ensure everything works: `python -m pytest test_calculator.py`

## Development Guidelines

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all public methods
- Include type hints where appropriate

### Testing
- Write unit tests for all new functionality
- Ensure tests cover edge cases and error conditions
- All tests must pass before submitting a PR
- Run tests with: `python -m pytest test_calculator.py -v`

### Making Changes

1. Create a new branch for your feature: `git checkout -b feature-name`
2. Make your changes following the code style guidelines
3. Add tests for new functionality
4. Run all tests to ensure they pass
5. Update documentation if needed
6. Commit your changes with a clear commit message
7. Push to your fork and create a pull request

### Pull Request Process

1. Fill out the pull request template completely
2. Ensure all tests pass and CI checks succeed
3. Request review from maintainers
4. Address any feedback from reviewers
5. Once approved, your PR will be merged

### Examples of Good Contributions

- Adding new mathematical operations (modulo, factorial, etc.)
- Improving error handling and validation
- Adding more comprehensive tests
- Improving documentation and docstrings
- Performance optimizations

### What to Avoid

- Breaking existing functionality
- Adding unnecessary dependencies
- Removing or modifying existing tests without good reason
- Large changes without prior discussion

## Questions?

If you have questions about contributing, please open an issue for discussion.
