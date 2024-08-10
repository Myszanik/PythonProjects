# GameDevelopmentScripts

The GameDevelopmentScripts folder focuses on the creation of basic games using Python. These games range from text-based adventures to simple GUI-based games.

## Included Scripts

### text_adventure_game.py
**Description:** A text-based adventure game where the player navigates through various scenarios based on their choices.  
**Usage:** Run the script to start the adventure. The game will prompt the user to make choices that guide the story.  
**Main Classes:**
- `StoryNode`: Represents a node in the story, holding the text and options for the next steps.
- `AdventureGameGUI`: Manages the GUI for the game, displaying the current node's text and options to the player.

### play_your_cards_right.py
**Description:** A card game where the player guesses if the next card will be higher or lower than the current card.  
**Usage:** Run the script and follow the prompts to play the game. The game will keep track of the score and provide options to continue or quit.  
**Main Functions:**
- `card_value(card)`: Converts face cards into their numeric values.
- `play_your_cards_right()`: Contains the main game logic, including the card deck setup and player interaction.

### animal_vegetable_game.py
**Description:** A simple GUI-based game where the user thinks of an animal or vegetable, and the game attempts to guess it based on yes/no questions.  
**Usage:** Run the script to start the game. The GUI will guide the player through a series of questions to determine their choice.  
**Main Class:**
- `AnimalVegetableGame`: Manages the GUI and the logic for guessing the player's choice based on their responses.
