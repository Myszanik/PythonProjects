import tkinter as tk

class AnimalVegetableGame:
    def __init__(self, master):
        # Set up the main window
        self.master = master
        master.title("Animal and Vegetable Guessing Game")
        master.geometry("400x350")

        # Welcome and instruction labels
        self.label = tk.Label(master, text="Welcome to the Animal and Vegetable Guessing Game!")
        self.label.pack(pady=10)

        self.instruction = tk.Label(master, text="Choose either Ostrich, Lion, Fish, Whale,\nCarrot, Broccoli, Peas, or Sweetcorn")
        self.instruction.pack(pady=10)

        # Initial question
        self.question_label = tk.Label(master, text="Is your choice an animal?")
        self.question_label.pack(pady=10)

        # Buttons for user responses
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.yes_button = tk.Button(self.button_frame, text="Yes", command=lambda: self.answer("y"))
        self.yes_button.pack(side=tk.LEFT, padx=10)

        self.no_button = tk.Button(self.button_frame, text="No", command=lambda: self.answer("n"))
        self.no_button.pack(side=tk.LEFT, padx=10)

        # Result label and restart button (initially hidden)
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)
        self.restart_button.pack_forget()

        self.state = "start"

    def answer(self, response):
        # Handle user responses and update questions
        if self.state == "start":
            if (response == "y"):
                self.question_label.config(text="Does the animal live in the water?")
                self.state = "animal_water"
            else:
                self.question_label.config(text="Is the vegetable green?")
                self.state = "vegetable_green"
        elif self.state == "animal_water":
            if response == "y":
                self.question_label.config(text="Is the animal a mammal?")
                self.state = "animal_mammal"
            else:
                self.question_label.config(text="Does the animal have wings?")
                self.state = "animal_wings"
        elif self.state == "animal_mammal":
            if response == "y":
                self.end_game("It must be a Whale!")
            else:
                self.end_game("It must be a Fish!")
        elif self.state == "animal_wings":
            if response == "y":
                self.end_game("It must be an Ostrich!")
            else:
                self.end_game("It must be a Lion!")
        elif self.state == "vegetable_green":
            if response == "y":
                self.question_label.config(text="Does the vegetable look like a tree?")
                self.state = "vegetable_tree"
            else:
                self.question_label.config(text="Is the vegetable orange?")
                self.state = "vegetable_orange"
        elif self.state == "vegetable_tree":
            if response == "y":
                self.end_game("It must be a Broccoli!")
            else:
                self.end_game("It must be Peas!")
        elif self.state == "vegetable_orange":
            if response == "y":
                self.end_game("It must be a Carrot!")
            else:
                self.end_game("It must be Sweetcorn!")

    def end_game(self, message):
        # Display the final result and show the restart button
        self.question_label.config(text="")
        self.result_label.config(text=message)
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.restart_button.pack()

    def restart_game(self):
        # Restart the game to its initial state
        self.state = "start"
        self.question_label.config(text="Is your choice an animal?")
        self.result_label.config(text="")
        self.yes_button.pack(side=tk.LEFT, padx=10)
        self.no_button.pack(side=tk.LEFT, padx=10)
        self.restart_button.pack_forget()

# Run the game
root = tk.Tk()
game = AnimalVegetableGame(root)
root.mainloop()

