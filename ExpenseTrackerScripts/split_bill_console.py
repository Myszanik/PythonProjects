import math

print("---Welcome to Split My Bill---")

# Get the number of pizzas
print("How many pizzas did your party have?")
while True:
    try:
        pizzas = int(input())  # Input for the number of pizzas
        break  
    except ValueError:
        print("Invalid input! You must enter a number.")

# Get the number of slices per pizza
print("What was the total number of slices on each pizza?")
while True:
    try:
        slices = int(input())  # Input for the number of slices per pizza
        break
    except ValueError:
        print("Invalid input! You must enter a number.")
        
# Get the number of people
print(f"How many people shared the {pizzas} pizza/pizzas?")
while True:
    try:
        people = int(input())  # Input for the number of people sharing the pizzas
        break  
    except ValueError:
        print("Invalid input! You must enter a number.")

# Calculate slices per person and remaining slices
slices_per_person = slices * pizzas / people
print(f"Total slices per person is {math.floor(slices_per_person)} slices")  # Floor value to get whole slices per person

slices_remaining = slices * pizzas - math.floor(slices_per_person) * people
print(f"Total slices left is {slices_remaining}")  # Calculate and print remaining slices

# Get the total bill amount
print("What was the total bill amount in £?")
while True:
    try:
        bill_total = float(input())  # Input for the total bill amount
        break
    except ValueError:
        print("Invalid input! You must enter a number.")

# Get the tip percentage
print("What percentage tip would you like to leave?")
tip_percentage = int(input())

# Calculate total bill including tip
bill_total_with_tip = bill_total + (tip_percentage / 100) * bill_total  # Calculate the total bill including tip
bill_total_with_tip = round(bill_total_with_tip, 1)  # Round to one decimal point

# Calculate cost per person
cost_per_person = bill_total_with_tip / people  # Calculate cost per person
cost_per_person = round(cost_per_person, 1)  # Round to one decimal point

# Print the final amounts
print(f"Total bill including tip is £{bill_total_with_tip}")
print(f"Total cost per person is £{cost_per_person}")

