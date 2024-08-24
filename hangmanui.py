class HangmanUI:
    def __init__(self, word):
        self.word = word
        self.guesses = set()
        self.incorrect_guesses = 0

    def display_hangman(self):
        incorrect_guesses = len(self.guesses - set(self.word))
        print(HANGMAN_STAGES[incorrect_guesses])

    def display_word_status(self):
        display_word = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        print(f"Word: {display_word}")

    def display_end_game_message(self, player_quit=False):
        if player_quit:
            print("Sorry to see you go!")
        else:
            print("Awesome! You guessed the word correctly!")

# Define the hangman stages
HANGMAN_STAGES = [
    """
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    ------------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   
    |
    -----------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   
    |
    -----------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   
    |
    -----------
    """,
    """
    ------
    |    |
    |    O
    |   /
    |   
    |
    -----------
    """,
    """
    ------
    |    |
    |    O
    |   
    |   
    |
    ----------
    """,
    """
    ------
    |    |
    |    
    |   
    |   
    |
    ----------
    """,
    """
    ------
    |    
    |    
    |   
    |   
    |
    ----------
    """
]

# Example usage:
hangman_game = HangmanUI("island")
hangman_game.display_word_status()  # Displays "_ _ _ _ _ _"
hangman_game.guesses.add("i")
hangman_game.display_word_status()  # Displays "i _ _ _ _ _"

remaining_attempts = 3
hangman_game.display_hangman()
