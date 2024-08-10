import math
import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to get the input from the user
def get_input(prompt):
    return simpledialog.askstring("Input", prompt)

# Function to get numerical input from the user
def get_numerical_input(prompt):
    while True:
        try:
            value = simpledialog.askstring("Input", prompt)
            return int(value)
        except ValueError:
            messagebox.showerror("Invalid input", "You must enter a number.")

# Initialize the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Lists to store prices and names
pizza_prices = []
names = []

# Welcome message
messagebox.showinfo("---Welcome to Split My Bill---")

# Get the number of pizzas
pizzas = get_numerical_input("How many pizzas did your party have?")

# Get the total number of slices per pizza
slices = get_numerical_input("What was the total number of slices on each pizza?")

# Get the number of people
people = get_numerical_input(f"How many people shared the {pizzas} pizza/pizzas?")

# Get the price of each pizza
for i in range(pizzas):
    price = simpledialog.askstring("Input", f"Price of pizza {i+1}: £")
    pizza_prices.append(float(price))

# Get the name of each person
for k in range(people):
    name = get_input(f"Name of person {k+1}:")
    names.append(name)

# Get the number of slices each person had from each pizza
def get_slices_per_person(pizzas, people, slices):
    slices_per_person = []
    for p in range(pizzas):
        while True:
            slices_info = []
            for k in range(people):
                person_slices = get_numerical_input(f"Enter the number of slices {names[k]} had from pizza {p+1}:")
                slices_info.append(person_slices)
            if sum(slices_info) != slices:
                messagebox.showerror("Error", f"Total slices entered do not match the expected {slices} slices for pizza {p+1}. Please enter again.")
            else:
                slices_per_person.append(slices_info)
                break
    return slices_per_person

slices_per_person = get_slices_per_person(pizzas, people, slices)

# Calculate the total slices each person had
def calculate_slices_per_person(slices_per_person):
    total_slices_per_person = []
    for i in range(people):
        total_slices = sum([slices_per_person[p][i] for p in range(pizzas)])
        total_slices_per_person.append(total_slices)
        messagebox.showinfo("Info", f"{names[i]} had {total_slices} slices in total.")
    return total_slices_per_person

total_slices_per_person = calculate_slices_per_person(slices_per_person)

# Calculate the cost each person has to pay
def calculate_cost_per_person(pizza_prices, slices_per_person, tip_percentage):
    total_cost_per_person = []
    bill_total = sum(pizza_prices)
    bill_total_with_tip = bill_total + (tip_percentage / 100) * bill_total
    messagebox.showinfo("Total Bill", f"\nTotal bill including tip is £{bill_total_with_tip:.2f}\n")

    for i in range(people):
        person_cost = sum([slices_per_person[p][i] * pizza_prices[p] / slices for p in range(pizzas)])
        person_cost_with_tip = person_cost + (tip_percentage / 100) * person_cost
        total_cost_per_person.append(person_cost_with_tip)
        messagebox.showinfo("Cost per Person", f"{names[i]}: Total cost is £{person_cost_with_tip:.2f}")

    return total_cost_per_person

# Ask for the tip percentage
tip_percentage = get_numerical_input("What percentage tip would you like to leave?")

calculate_cost_per_person(pizza_prices, slices_per_person, tip_percentage)

# Close the main application window
root.destroy()

pizza_prices = []  # List to store the prices of the pizzas
names = []  # List to store the names of the people

print("---Welcome to Split My Pizza Bill---")  # Display a welcome message

def pizza_slices_and_people_info():
    # Prompt for and handle input for the number of pizzas
    print("How many pizzas did your party have?")
    while True:
        try:
            pizzas = int(input()) 
            break  
        except ValueError:
            print("Invalid input! You must enter a number.")

    # Prompt for and handle input for the total number of slices on the pizza
    print("What was the total number of slices on each pizza?")
    while True:
        try:
            slices = int(input())  # Convert user input to an integer
            break  # Exit the loop if input is successfully converted
        except ValueError:
            print("Invalid input! You must enter a number.")  # Prompt again if input is not a number

    # Prompt for and handle input for the number of people sharing
    print(f"How many people shared the {pizzas} pizza/pizzas?")
    while True:
        try:
            people = int(input()) 
            break  
        except ValueError:
            print("Invalid input! You must enter a number.") 

    return pizzas, slices, people  # Return the values of pizzas, slices, and people

pizzas, slices, people = pizza_slices_and_people_info()

def pizza_price(pizzas):
    print("Enter the price of each pizza:")
    # Prompt for and handle input for the price of each pizza
    for i in range(pizzas):
        while True:
            try:
                price = float(input(f"Price of pizza {i+1}: £"))
                pizza_prices.append(price)
                break
            except ValueError:
                print("Invalid input! You must enter a number.")

pizza_price(pizzas)

def names_of_people(people):
    print("Enter the name of each person:")
    # Prompt for and handle input for the name of each person
    for k in range(people):
        while True:
            try:
                name = str(input(f"Name of person {k+1}: "))
                names.append(name)
                break
            except ValueError:
                print("Invalid input! You must enter a name.")

names_of_people(people)

def get_slices_per_person(pizzas, people, slices):
    slices_per_person = []
    for p in range(pizzas):
        while True:
            slices_info = []
            for k in range(people):
                while True:
                    try:
                        slice = int(input(f"Enter the number of slices {names[k]} had from pizza {p+1}: "))
                        slices_info.append(slice)
                        break
                    except ValueError:
                        print("Invalid input! You must enter a number.")
            if sum(slices_info) != slices:
                print(f"Total slices entered do not match the expected {slices} slices for pizza {p+1}. Please enter again.")
            else:
                slices_per_person.append(slices_info)
                break  # Exit the loop if the input is correct for the current pizza
    return slices_per_person

slices_per_person = get_slices_per_person(pizzas, people, slices)

def calculate_slices_per_person(slices, pizzas, people):
    # Calculate slices per person by dividing total slices (slices * pizzas) by number of people
    slices_per_person = slices * pizzas / people
    # Display the number of slices each person gets (floor value of slices_per_person)
    print(f"Total slices per person is {math.floor(slices_per_person)} slices")

calculate_slices_per_person(slices, pizzas, people)

def calulate_slices_remaining(slices, pizzas, people):
    # Calculate remaining slices by subtracting the floor value of slices_per_person times people from total slices times pizzas
    slices_per_person = slices * pizzas / people
    slices_remaining = slices * pizzas - math.floor(slices_per_person) * people
    # Display the total number of slices left after distribution
    print(f"Total slices left is {slices_remaining}")

calulate_slices_remaining(slices, pizzas, people)

def calculate_cost_per_person(pizza_prices):
    print("What percentage tip would you like to leave?")
    tip_percentage = int(input())
    bill_total = sum(pizza_prices)
    bill_total = bill_total + (tip_percentage / 100) * bill_total

    cost_per_person = bill_total / people

    print(f"Total bill including tip is £{bill_total}")
    print(f"Total cost per person is £{cost_per_person}")

calculate_cost_per_person(pizza_prices)
