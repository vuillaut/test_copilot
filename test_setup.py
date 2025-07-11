#!/usr/bin/env python3
"""
Test script to verify the repository setup is working correctly.
Run this script to ensure everything is properly configured.
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and print the result."""
    print(f"\n🔍 {description}")
    print(f"Command: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            cwd=Path(__file__).parent
        )
        
        if result.returncode == 0:
            print("✅ SUCCESS")
            if result.stdout:
                print(result.stdout)
        else:
            print("❌ FAILED")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    return True

def main():
    """Run all verification tests."""
    print("🚀 Testing GitHub Copilot Repository Setup")
    print("=" * 60)
    
    tests = [
        ("python --version", "Checking Python version"),
        ("python -m pytest --version", "Checking pytest installation"),
        ("python calculator.py", "Running calculator demo"),
        ("python -m pytest test_calculator.py -v", "Running basic calculator tests"),
        ("python -m pytest examples/test_scientific_calculator.py -v", "Running scientific calculator tests"),
        ("python -c 'from calculator import Calculator; print(\"Calculator import works!\")'", "Testing calculator import"),
    ]
    
    all_passed = True
    for command, description in tests:
        if not run_command(command, description):
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! Repository is ready for GitHub Copilot testing.")
        print("\n📋 Next steps:")
        print("1. Commit and push all files to GitHub")
        print("2. Create test branches with problematic code")
        print("3. Open PRs to test Copilot's review capabilities")
        print("4. Check that Copilot flags issues according to .github/copilot-instructions.md")
    else:
        print("❌ Some tests failed. Please fix the issues before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main()
