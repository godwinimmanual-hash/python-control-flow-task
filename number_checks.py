"""
number_checks.py

A simple script that takes an integer input from the user and reports:
1. Whether the number is even or odd.
2. Whether the number is positive, negative, or zero.

This demonstrates basic conditional logic (if / elif / else) in Python.
"""


def check_even_odd(number: int) -> str:
    """Return 'Even' if the number is divisible by 2, otherwise 'Odd'."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_sign(number: int) -> str:
    """Return whether the number is Positive, Negative, or Zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def get_integer_input(prompt: str) -> int:
    """
    Repeatedly prompt the user until a valid integer is entered.
    Handles invalid input gracefully (e.g., letters, decimals, empty input).
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 5, -3, 0).")


def main():
    print("=== Number Classification Tool ===")
    number = get_integer_input("Enter an integer: ")

    even_odd_result = check_even_odd(number)
    sign_result = check_sign(number)

    print(f"\nResults for {number}:")
    print(f"  - Even/Odd : {even_odd_result}")
    print(f"  - Sign     : {sign_result}")

    # Special-case note for zero, since zero is technically even,
    # but it's neither positive nor negative.
    if number == 0:
        print("  Note: Zero is even, but it's neither positive nor negative.")


if __name__ == "__main__":
    main()
