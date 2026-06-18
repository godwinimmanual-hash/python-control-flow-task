# Conditional Statements & Loops in Python

This repository contains my solutions for the "Conditional Statements & Loops in
Python" internship task. It demonstrates control flow in Python using
conditional statements (`if` / `elif` / `else`) and loops (`for` / `while`).

## Project Structure

```
.
├── README.md
├── .gitignore
├── src/
│   ├── number_checks.py      # Even/Odd and Positive/Negative/Zero classifier
│   └── loop_operations.py    # Multiplication table, sum of N numbers, triangle pattern
└── docs/
    ├── control_flow_report.pdf   # Written report on logic & loop differences
    └── screenshots/              # Terminal output screenshots
```

## How to Run

Requires Python 3.7+.

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. Run the number classification script:
   ```
   python3 src/number_checks.py
   ```
   You'll be prompted to enter an integer. The script reports whether it's
   even/odd and positive/negative/zero.

3. Run the loop operations script:
   ```
   python3 src/loop_operations.py
   ```
   You'll be prompted for:
   - A number to generate its multiplication table (1–10)
   - A value N to compute the sum of the first N natural numbers
   - A number of rows to print a right-angled triangle of asterisks

## What I Learned

- How `if` / `elif` / `else` branches control program flow based on conditions.
- The difference between `for` loops (iterating a known number of times /
  over a sequence) and `while` loops (repeating until a condition becomes
  false) — and when to choose one over the other.
- How nested loops can be used to build 2D patterns like triangles.
- How to validate user input defensively (handling non-numeric input,
  negative numbers, and zero as edge cases) so the program doesn't crash.
- The importance of writing small, well-documented, reusable functions
  rather than one large script.

## Testing Notes

Both scripts were tested with the following edge cases:
- Zero (`0`)
- Negative numbers (e.g., `-3`)
- Positive numbers (e.g., `5`, `7`)
- Invalid/non-numeric input (handled with a retry loop)

Screenshots of these test runs are available in `docs/screenshots/`.
