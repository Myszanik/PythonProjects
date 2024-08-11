import tkinter as tk
from tkinter import simpledialog, messagebox
import tkinter.scrolledtext as scrolledtext
import textwrap

class StoryNode:
    def __init__(self, text):
        self.text = text
        self.options = []

    def add_option(self, option_text, next_node):
        self.options.append((option_text, next_node))

    def get_next_node(self, choice):
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(self.options):
                _, next_node = self.options[idx]
                return next_node
        return None

    def get_text(self):
        return self.text

    def get_options(self):
        return [option_text for option_text, _ in self.options]


def create_story(name):
    start = StoryNode(f"Greetings {name}! If you are brave enough, we can interest you with some contracts "
                      "that can send you on some epic adventures:")

    # Adventure descriptions with text wrapping
    dragons_bane_desc = textwrap.fill(
        "Brave adventurers needed to confront and defeat the fearsome dragon Drakenroth, whose fiery wrath threatens all of Eldoria. "
        "Embark on a perilous journey through the Cursed Forest, Ancient Ruins, and the treacherous Mountain of Doom, facing deadly foes along the way. "
        "Only the strongest and most courageous need apply, for this quest requires great valor and skill.",
        width=70
    )

    scavenger_hunt_desc = textwrap.fill(
        "Seekers of powerful artifacts are required to gather three ancient relics to aid in the battle against Drakenroth. "
        "Your journey will take you to the Whispering Caves, the Sunken Temple, and the Eldorian Church, each guarded by formidable creatures. "
        "This quest demands resourcefulness and determination to uncover the secrets and harness the power needed to save Eldoria.",
        width=70
    )

    # Scavenger Hunt Nodes
    scavenger_hunt = StoryNode(scavenger_hunt_desc)

    # Initial Church Node as part of the Scavenger Hunt
    church_adventure_desc = textwrap.fill(
        "You arrive at the ancient and solemn Eldorian Church. One of the relics is rumored to be hidden here. "
        "Will you search it for clues, or seek the wisdom of the resident priest?",
        width=70
    )
    church_adventure = StoryNode(church_adventure_desc)

    # Expanded church nodes
    search_altar = StoryNode("You approach the altar and find a series of strange symbols etched into the stone. "
                             "Deciphering them reveals directions to a hidden statue within the church.")

    statue_clue = StoryNode("You find the statue and discover a hidden compartment that mentions a secret basement beneath the church. "
                            "However, the basement appears to be locked. You'll need to find a key to access it.")

    key_search = StoryNode("You need to find a key to unlock the hidden basement. You have three places to search:")
    search_desk = StoryNode("You search the desk in the church’s study but find nothing useful.")
    search_shelf = StoryNode("You check the shelves in the church’s library but come up empty.")
    search_chest = StoryNode("You open an old chest in the corner and find a key that might unlock the hidden basement.")

    # Nodes for finding the key
    key_found = StoryNode("You use the key to unlock the hidden basement. As you prepare to enter, you notice the priest nearby.")

    # Decision to go alone or with the priest
    go_alone = StoryNode("You decide to venture into the basement alone. The air is thick with dust and the scent of ancient secrets. "
                         "As you descend the stairs, you hear faint whispers echoing through the darkness. "
                         "Your courage is tested as you step into the unknown...")

    take_priest = StoryNode("You ask the priest to join you. He agrees, and together you enter the basement. "
                            "With the priest's knowledge of the church's history, he helps you avoid traps and decipher ancient texts. "
                            "The basement reveals a hidden chamber where you find the relic, a powerful artifact that will aid in your quest.")

    # Connect nodes with options
    start.add_option("The Dragon's Bane", dragons_bane_desc)
    start.add_option("The Scavenger Hunt", scavenger_hunt)

    scavenger_hunt.add_option("Go to the Eldorian Church", church_adventure)

    church_adventure.add_option("Search the altar", search_altar)

    search_altar.add_option("Investigate the statue", statue_clue)

    statue_clue.add_option("Search for the key", key_search)

    key_search.add_option("Search the desk", search_desk)
    key_search.add_option("Check the shelves", search_shelf)
    key_search.add_option("Open the chest", search_chest)

    search_desk.add_option("Return to search for the key", key_search)
    search_shelf.add_option("Return to search for the key", key_search)
    search_chest.add_option("Use the key to unlock the hidden basement", key_found)

    key_found.add_option("Go alone", go_alone)
    key_found.add_option("Take the priest with you", take_priest)

    return start


class AdventureGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")
        self.current_node = None

        # Create text entry for name and initialize game interface
        self.name_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)

        self.name_label = tk.Label(self.name_frame, text="Welcome adventurer in our guild in Eldoria! What shall we call you?")
        self.name_label.pack(padx=10, pady=5)

        self.name_entry = tk.Entry(self.name_frame)
        self.name_entry.pack(padx=10, pady=5)

        self.submit_button = tk.Button(self.name_frame, text="Start Adventure", command=self.submit_name)
        self.submit_button.pack(padx=10, pady=5)

        self.name_frame.pack(padx=10, pady=10)
        
        # Initialize other attributes
        self.player_name = None
        self.text_display = None
        self.option_buttons = []
        self.starting_node = None
        self.initialize_game_interface()

    def submit_name(self):
        self.player_name = self.name_entry.get()
        if self.player_name:
            self.name_frame.pack_forget()
            self.game_frame.pack(padx=10, pady=10)
            self.starting_node = create_story(self.player_name)
            self.current_node = self.starting_node
            self.update_text_display()
            self.create_option_buttons()
        else:
            messagebox.showerror("Error", "Name cannot be empty. Please enter a valid name.")

    def initialize_game_interface(self):
        self.text_display = scrolledtext.ScrolledText(self.game_frame, width=80, height=15, wrap=tk.WORD)
        self.text_display.pack(padx=10, pady=10)

    def create_option_buttons(self):
        options = self.current_node.get_options()
        for idx, option_text in enumerate(options, 1):
            button = tk.Button(self.game_frame, text=f"Option {idx}: {option_text}", command=lambda idx=idx: self.choose_option(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def update_text_display(self):
        text = self.current_node.get_text()
        self.text_display.delete('1.0', tk.END)
        self.text_display.insert(tk.END, text)

    def choose_option(self, idx):
        options = self.current_node.get_options()
        next_node = self.current_node.get_next_node(str(idx))
        if callable(next_node):
            next_node = next_node()
        if next_node:
            self.current_node = next_node
            self.update_text_display()

            # Remove current option buttons
            for button in self.option_buttons:
                button.pack_forget()
            self.option_buttons.clear()

            # Create new option buttons for the next node
            self.create_option_buttons()

        else:
            # Final node reached or confirmation node
            confirmation = messagebox.askquestion("Adventure Confirmation",
                                                     f"Are you sure you want to choose '{options[idx - 1]}'?")
            if confirmation == 'yes':
                messagebox.showinfo("Adventure Confirmed", "Your adventure begins!")
            else:
                # Restart game
                self.current_node = self.starting_node
                self.update_text_display()
                self.create_option_buttons()




if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureGameGUI(root)
    root.mainloop()
