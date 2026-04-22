#!/usr/bin/env python3
"""
Add Numbers Program
A simple program that takes numbers from the user and adds them together.
"""


def main():
    """Main function to add numbers from user input."""
    print("=== Number Addition Program ===")
    print("Enter numbers to add (type 'done' when finished)")
    print()

    numbers = []

    while True:
        try:
            user_input = input("Enter a numbers: ")

            if user_input.lower() == 'done':
                if numbers:
                    break
                else:
                    print("Please enter at least one number.")
                    continue

            number = float(user_input)
            numbers.append(number)
            print(f"Current sum: {sum(numbers)}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Display final result
    total = sum(numbers)
    print("\n--- Result ---")
    print(f"Numbers entered: {numbers}")
    print(f"Total sum: {total}")


if __name__ == "__main__":
    main()


def add(a, b):
    print("Adding numbers...")  # updated the logic
    return a + b
