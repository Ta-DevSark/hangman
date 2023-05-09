class hangman:
    def __init__(self, word):
        self.word = word
        self.possible_words = ['rambunctious','serendipity','miscellaneous','becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(word)
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(self.word)

     
        def guess_letter(self, letter):
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter

        """
        self.guessed_word = []
        self.guessed_word_count = 0
        self.word_length = len(self.word)
        self.guessed_word_length = len(self.guessed_word)
        self.guessed_letters_length = len(self.guessed_letters)
        self.guessed_letters_count = self.guessed_letters_length
        self.guessed_word_count = self.guessed_word_length
        """

"""
- A `wrongly_guessed_letters` attribute that contains a list of strings where each 
element will be a letter guessed by the user that is not in the `word_to_find`.
- A `turn_count` attribute that contain the number of turns played by the player. 
This will be represented as an `int`.

- An `error_count` attribute that contains the number of errors made by the player.

- A `play()` method that asks the player to enter a letter. 
Be careful that the player shouldn't be allowed to type something else than a letter, and not more than a letter. 
If the player guessed a letter well, add it to the `correctly_guessed_letters` list. 
If not, add it to the `wrongly_guessed_letters` list and add 1 to `error_count`.

- A `start_game()` method that:
  - will call `play()` until the game is over (because the use guessed the word or because of a game over).
  - will call `game_over()` if `lives` is equal to 0.
  - will call `well_played()` if all the letter are guessed.
  - will print `correctly_guessed_letters`, `bad_guessed_letters`, `life`, `error_count` and `turn_count` at the end of each turn.

- A `game_over()` method that will stop the game and print `game over...`.

- A `well played()` method that will print `You found the word: {word_to_find_here} 
in {turn_count_here} turns with {error_count_here} errors!`.
"""