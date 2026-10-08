def get_total_expenses():
    total = 0

    while True:
        entry = input("Enter expense amount (or 'done' to finish): ").strip()

        if entry.lower() == "done":
            break

        try:
            expense = float(entry)
        except ValueError:
            print("Invalid input! Please enter a number or 'done'.")
            continue

        if expense < 0:
            print("Expense cannot be negative. Try again.")
            continue

        total += expense
        print(f"Added {expense:.2f}. Running total: {total:.2f}")
        print("=" * 40)

    return total


def display_total(total):
    print("=" * 40)
    print(f"FINAL TOTAL: ${total:.2f}")
    print("=" * 40)


def main():
    print("=" * 40)
    print("Expense Tracker")
    print("=" * 40)

    total = get_total_expenses()
    display_total(total)


if __name__ == "__main__":
    main()
