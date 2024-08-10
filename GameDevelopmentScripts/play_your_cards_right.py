import random

def card_value(card):
    """Convert card face to its numerical value."""
    card_number = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}  # Face cards values
    return card_number.get(card, card)  # Return number or face card value

def play_your_cards_right():
    """Play the 'Play Your Cards Right' game."""
    while True:
        # Initialize the deck and shuffle
        deck = (list(range(2, 11)) + ['J', 'Q', 'K', 'A']) * 4
        random.shuffle(deck)

        current_card = deck.pop()  # Draw the first card
        score = 0  # Initialize score
        game_active = True

        print("Welcome to 'Play Your Cards Right'!")
        print("Guess if the next card will be higher or lower than the current card.")
        print(f"The starting card is: {current_card}")

        while game_active and len(deck) > 0:
            guess = input("Will the next card be higher or lower? (h/l): ")
            if guess not in ['h', 'l']:
                print("Invalid input. Enter 'h' for higher or 'l' for lower.")
                continue

            next_card = deck.pop()  # Draw the next card
            print(f"Next card is: {next_card}")

            # Check if the guess was correct
            if (guess == 'h' and card_value(next_card) > card_value(current_card)) or (guess == 'l' and card_value(next_card) < card_value(current_card)):
                score += 1
                print("Correct guess! Your score is:", score)
                current_card = next_card
                continue_game = input("Do you want to continue? (y/n) ").lower()
                if continue_game != 'y':
                    game_active = False
            
            else:
                print("Wrong guess! Game over, your score was:", score)
                break
                
        restart_game = input("Would you like to restart the game? (y/n) ").lower()
        if restart_game != 'y':
            break

if __name__ == "__main__":
    play_your_cards_right()
