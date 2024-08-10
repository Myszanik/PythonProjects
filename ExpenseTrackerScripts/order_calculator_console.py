total_cost = 0.00

# Base options
print("Choose your crust:")
print("1. Thick crust (£8.00)")
print("2. Thin crust (£10.00)")
crust_choice = input("Enter your choice (1 or 2): ")

# Size options
print("\nChoose your size:")
print("1. 8 inch")
print("2. 10 inch")
print("3. 12 inch (+£2.00)")
print("4. 14 inch (+£2.00)")
print("5. 18 inch (+£2.00)")
size_choice = input("Enter your choice (1 to 5): ")

# Cheese option
cheese_choice = input("\nWould you like cheese? (yes/no): ").lower()
if cheese_choice == "no":
    total_cost -= 0.50

# Type of pizza
print("\nChoose your type of pizza:")
print("1. Margarita")
print("2. Vegetable (+£1.00)")
print("3. Vegan (+£1.00)")
print("4. Hawaiian (+£2.00)")
print("5. Meat feast (+£2.00)")
pizza_type_choice = input("Enter your choice (1 to 5): ")

# Voucher code check
voucher_code = input("\nDo you have a voucher code? Enter it here (leave blank if none): ")
if size_choice == "5" and voucher_code.lower() == "funfriday":
    total_cost -= 2.00

# Calculate total cost based on user choices
if crust_choice == "1":
    total_cost += 8.00
elif crust_choice == "2":
    total_cost += 10.00

if size_choice in ["3", "4", "5"]:
    total_cost += 2.00

if pizza_type_choice in ["2", "3"]:
    total_cost += 1.00
elif pizza_type_choice in ["4", "5"]:
    total_cost += 2.00

# Display the total cost to the user
print(f"\nYour total cost for the pizza is: £{total_cost:.2f}")
