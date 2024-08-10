import tkinter as tk
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


def create_story():
    # Define the nodes of your story
    name = input("Welcome adventurer in our guild in Eldoria! What shall we call you? ")
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
        "Your journey will take you to the Whispering Caves, the Sunken Temple, and the Sky Tower, each guarded by formidable creatures. "
        "This quest demands resourcefulness and determination to uncover the secrets and harness the power needed to save Eldoria.",
        width=70
    )

    forest_adventure_desc = textwrap.fill(
        "You find yourself at the edge of the dark and mysterious Haunted Forest. Do you dare venture deeper, or take a safer route around?",
        width=70
    )

    church_adventure_desc = textwrap.fill(
        "You arrive at the ancient and solemn Eldorian Church. Will you search it for clues, or seek the wisdom of the resident priest?",
        width=70
    )

    # Create StoryNode instances for adventures and their descriptions
    the_dragons_bane = StoryNode(dragons_bane_desc)
    the_scavenger_hunt = StoryNode(scavenger_hunt_desc)
    forest_adventure = StoryNode(forest_adventure_desc)
    church_adventure = StoryNode(church_adventure_desc)

    # Link nodes with choices
    start.add_option("The Dragon's Bane", the_dragons_bane)
    start.add_option("The Scavenger Hunt", the_scavenger_hunt)

    the_dragons_bane.add_option("yes", forest_adventure)
    the_dragons_bane.add_option("no", start)

    the_scavenger_hunt.add_option("yes", church_adventure)
    the_scavenger_hunt.add_option("no", start)

    forest_adventure.add_option("Venture deeper into the forest", StoryNode("You decide to delve deeper into the Haunted Forest. What's your next move?"))
    forest_adventure.add_option("Go around the forest", StoryNode("You choose to take a safer path around the Haunted Forest. What's your next move?"))

    church_adventure.add_option("Search the church for clues", StoryNode("You decide to search the Eldorian Church for any hidden clues. What's your next move?"))
    church_adventure.add_option("Ask the priest for history of the place", StoryNode("You opt to seek the wisdom of the priest regarding the history of Eldoria. What's your next move?"))
    # NOW IT WORKS, YOU I JUST NEED TO KEEP ADDING MORE ADVENTURES TO IT SO IT HAS MORE STORY IN IT.
    # ADD SOME FIGHTS, INTRODUCE HEALTH BAR, DIALOGS WITH NPCs
    return start


class AdventureGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Adventure Game")
        self.current_node = None

        # Create story and set starting node
        self.starting_node = create_story()
        self.current_node = self.starting_node

        # Create text display area
        self.text_display = scrolledtext.ScrolledText(self.root, width=80, height=15, wrap=tk.WORD)
        self.text_display.pack(padx=10, pady=10)
        self.update_text_display()

        # Create option buttons
        self.option_buttons = []
        self.create_option_buttons()

    def create_option_buttons(self):
        options = self.current_node.get_options()
        for idx, option_text in enumerate(options, 1):
            button = tk.Button(self.root, text=f"Option {idx}: {option_text}", command=lambda idx=idx: self.choose_option(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

    def update_text_display(self):
        text = self.current_node.get_text()
        self.text_display.delete('1.0', tk.END)
        self.text_display.insert(tk.END, text)

    def choose_option(self, idx):
        options = self.current_node.get_options()
        next_node = self.current_node.get_next_node(str(idx))
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
            confirmation = tk.messagebox.askquestion("Adventure Confirmation",
                                                     f"Are you sure you want to choose '{options[idx - 1]}'?")
            if confirmation == 'yes':
                tk.messagebox.showinfo("Adventure Confirmed", "Your adventure begins!")
            else:
                # Restart game
                self.current_node = self.starting_node
                self.update_text_display()
                self.create_option_buttons()


if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureGameGUI(root)
    root.mainloop()
