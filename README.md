# DecodeLabs Python Expense Tracker

A command-line Expense Tracker built in Python as Project 2 of the
Python Programming Internship at Decode Labs.

## Features
- Enter expenses one at a time and see a running total after each entry
- Type `done` to finish and display the final total
- Input validation: rejects non-numeric input without crashing
- Rejects negative amounts
- Logic (`get_total_expenses`) is separated from display (`display_total`)

## How to Run
```bash
python expense_tracker.py
```

## Example
```
Enter expense amount (or 'done' to finish): 100
Added 100.00. Running total: 100.00
Enter expense amount (or 'done' to finish): 50
Added 50.00. Running total: 150.00
Enter expense amount (or 'done' to finish): done
FINAL TOTAL: $150.00
```

## What I Learned
- The accumulator pattern (`total += expense`), with `total` initialized outside the loop so it persists across iterations
- Converting `input()` strings to numbers before calculating
- Defensive coding with `try/except ValueError`
- Using a sentinel value (`done`) to exit a loop cleanly

## Tech Stack
Python 3 (standard library only)