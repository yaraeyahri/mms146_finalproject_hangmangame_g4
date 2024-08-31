class HangmanUI:
    def __init__(self, word):
        self.word = word
        self.guesses = set()
        self.incorrect_guesses = 0
        self.max_attempts = 6
        self.score = 0  # Show score

    def display_hangman(self):
        print(HANGMAN_STAGES[self.incorrect_guesses])

    def display_word_status(self):
        display_word = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        print(f"Word: {display_word}")

    def display_end_game_message(self, player_quit=False):
        if player_quit:
            print("Sorry to see you go!")
        else:
            print("Awesome! You guessed the word correctly!")
        print(f"Your final score: {self.score}")

    def get_user_guess(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
            else:
                return guess

    def play_game(self):
        while True:
            self.display_word_status()
            self.display_hangman()

            if self.incorrect_guesses >= self.max_attempts:
                print(f"Game over! The word was '{self.word}'.")
                self.display_end_game_message()
                break

            guess = self.get_user_guess()

            if guess in self.guesses:
                print("You already guessed that letter. Try again.")
            else:
                self.guesses.add(guess)
                if guess in self.word:
                    print("Correct guess!")
                    self.score += 10  # Add points for each correct guess
                else:
                    print("Incorrect guess.")
                    self.incorrect_guesses += 1
                    self.score -= 5  # Deduct points for each incorrect guess

            if all(letter in self.guesses for letter in self.word):
                print(f"Congratulations! You guessed the word '{self.word}' correctly!")
                self.display_end_game_message()
                break

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
if __name__ == "__main__":
    hangman_game = HangmanUI("island")
    hangman_game.play_game()
