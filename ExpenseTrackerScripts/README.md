# ExpenseTrackerScripts

The ExpenseTrackerScripts folder contains scripts that help manage and calculate the distribution of expenses among multiple people. The scripts are designed to assist in splitting bills fairly.

## Included Scripts

### split_my_bill_gui.py
**Description:** A GUI-based application that calculates how much each person owes based on the number of pizzas ordered, their prices, and the number of slices each person had.  
**Usage:** Run the script, and the GUI will prompt the user for details about the pizzas, slices, and people involved. It then calculates and displays each person's share of the bill, including tips.  
**Main Functions:**
- `get_input(prompt)`: Collects string input from the user via a dialog box.
- `get_numerical_input(prompt)`: Collects numerical input from the user, ensuring it is a valid number.
- `calculate_cost_per_person()`: Calculates and displays the cost each person needs to pay.

### split_bill_console.py
**Description:** A command-line version of the bill-splitting application, allowing the user to input data directly via the terminal.  
**Usage:** Run the script in a terminal, follow the prompts to enter the necessary information, and the script will calculate and display each person's share.  
**Main Functions:**
- `pizza_slices_and_people_info()`: Collects basic information about the pizzas, slices, and people.
- `get_slices_per_person()`: Collects the number of slices each person had from each pizza.
- `calculate_slices_per_person()`: Calculates and displays the total number of slices each person had.
- `calculate_cost_per_person()`: Calculates the cost each person needs to pay based on the slices they consumed.

### order_calculator_console.py
**Description:** A script that calculates the total cost of a pizza based on user-selected options such as crust type, size, cheese, type of pizza, and any applicable voucher codes.  
**Usage:** Run the script and follow the prompts to select your options. The script will calculate and display the total cost of the pizza.
**Main Functions:**
- `get_input(prompt)`: Collects string input from the user.
- `calculate_total_cost()`: Calculates the total cost based on selected options and applies any discounts.
