"""
loop_operations.py

A script that demonstrates loop-based mathematical operations and pattern
generation:
1. Prints a multiplication table for a user-defined number (using a for loop).
2. Calculates the sum of the first N natural numbers (using a while loop).
3. Prints a right-angled triangle pattern of asterisks (using nested for loops).
"""


def get_positive_integer_input(prompt: str) -> int:
    """
    Repeatedly prompt the user until a valid non-negative integer is entered.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 5, 10).")


def print_multiplication_table(number: int, upto: int = 10) -> None:
    """Print the multiplication table for `number` from 1 to `upto` using a for loop."""
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, upto + 1):
        print(f"  {number} x {i} = {number * i}")


def sum_of_natural_numbers(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers using a while loop.
    (Demonstrates while-loop logic, even though a formula could do this directly.)
    """
    total = 0
    counter = 1
    while counter <= n:
        total += counter
        counter += 1
    return total


def print_right_triangle(rows: int) -> None:
    """Print a right-angled triangle pattern of asterisks using nested for loops."""
    print(f"\nRight-Angled Triangle Pattern ({rows} rows):")
    for i in range(1, rows + 1):
        # Inner loop builds each row's asterisks
        line = ""
        for _ in range(i):
            line += "*"
        print(line)


def main():
    print("=== Loop Operations Tool ===")

    # 1. Multiplication table
    table_number = get_positive_integer_input(
        "Enter a number to generate its multiplication table: "
    )
    print_multiplication_table(table_number)

    # 2. Sum of first N natural numbers
    n = get_positive_integer_input(
        "\nEnter N to calculate the sum of the first N natural numbers: "
    )
    total = sum_of_natural_numbers(n)
    print(f"Sum of first {n} natural numbers = {total}")

    # 3. Right-angled triangle pattern
    rows = get_positive_integer_input(
        "\nEnter the number of rows for the triangle pattern: "
    )
    print_right_triangle(rows)


if __name__ == "__main__":
    main()
