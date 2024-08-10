# integer_input_validation.py
# This script prompts the user for two integer inputs, validates them, and then prints the sum of the two integers.

def is_integer(value):
    """Check if the input is an integer (a number without decimals)."""
    return value.isdigit()

def get_integer(prompt):
    """Keep asking the user for an integer until a valid one is entered."""
    while True:
        user_input = input(prompt)
        if is_integer(user_input):
            return int(user_input)
        else:
            print("That's not a valid number. Please try again.")

def main():
    num1 = get_integer("Enter the first number: ")
    num2 = get_integer("Enter the second number: ")
    print(f"The sum of {num1} and {num2} is {num1 + num2}")

if __name__ == "__main__":
    main()

