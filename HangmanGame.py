class HangmanGame:
    def __init__(self, secret_word: str, max_attempts: int = 7):
        self.secret_word = secret_word  # The word
        self.guessed_letters = []  # List of correct guesses
        self.incorrect_guesses = []  # List of incorrect guesses
        self.max_attempts = max_attempts  # Max number of allowed incorrect guesses

    def check_guess(self, guess: str) -> bool:
        if guess in self.secret_word:
            if guess not in self.guessed_letters:
                self.guessed_letters.append(guess)
            return True
        else:
            if guess not in self.incorrect_guesses:
                self.incorrect_guesses.append(guess)
            return False

    def update_hangman(self, guess: str) -> None:
        if guess in self.guessed_letters or guess in self.incorrect_guesses:
            print(f"You've already guessed '{guess}'. Try another letter.")
        elif self.check_guess(guess):
            print(f"Correct! '{guess}' is in the word.")
        else:
            print(f"Sorry! '{guess}' is not in the word.")

    def display_result(self) -> None:
        if self.word_guessed():
            print("Yey! You have guessed the word:", self.secret_word)
        else:
            print("Sorry, try again. The word was:", self.secret_word)

    def game_over(self) -> bool:
        return self.attempts_remaining() <= 0 or self.word_guessed()

    def attempts_remaining(self) -> int:
        return self.max_attempts - len(self.incorrect_guesses)

    def word_guessed(self) -> bool:
        return all(letter in self.guessed_letters for letter in self.secret_word)


# This is only for testing the class:
def test_hangman_game():
    game = HangmanGame("python")  # The secret word that must be guessed is "python".
    
    while not game.game_over():
        print("\nWord: ", " ".join([letter if letter in game.guessed_letters else "_" for letter in game.secret_word]))
        print("Guessed Letters: ", ", ".join(game.guessed_letters))
        print("Incorrect Guesses: ", ", ".join(game.incorrect_guesses))
        print(f"Attempts Remaining: {game.attempts_remaining()}")
        
        guess = input("Type a letter to guess the word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            game.update_hangman(guess)
        else:
            print("Please enter a single alphabetic character.")
    
    game.display_result()

test_hangman_game()
