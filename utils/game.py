class Hangman:
    def __init__(self, word):
        self.word = word
        self.possible_words = ['sunflower', 'pho','rambunctious','serendipity','miscellaneous','becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(word)
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(word)
        self.wrongly_guessed_letters = []
        """
        - A `wrongly_guessed_letters` attribute that contains a list of strings where each 
        element will be a letter guessed by the user that is not in the `word_to_find`.
        """
        self.turn_count= 0
        self.error_count = 0
     
        def play():
            guess = input("Enter a letter: ").upper()
            while self.lives > 0:
                guess = input("Enter a letter: ").upper()
                if guess in self.word_to_find:
                    print(f"{guess} is in the word!")
                    self.correctly_guessed_letters.append(guess)
                    self.turn_count += 1

                elif guess not in self.word_to_find:
                    print(f"{guess} is not in the word!")
                    self.wrongly_guessed_letters.append(guess)
                    self.lives -= 1
                    self.error_count += 1
                    self.turn_count += 1
                    
                elif len(guess) > 1 or guess != guess.isalpha():
                    print(f"{guess} is not a valid letter !")
                
                print(self.correctly_guessed_letters, self.wrongly_guessed_letters, self.lives,self.error_count, self.turn_count)

                


        def start_game():
            if lives == 0:
                print("Game over!")
        """
            - will call `play()` until the game is over (because the use guessed the word or because of a game over).
            - will call `game_over()` if `lives` is equal to 0.
            - will call `well_played()` if all the letter are guessed.
            - will print `correctly_guessed_letters`, `bad_guessed_letters`, `life`, `error_count` and `turn_count` at the end of each turn.
        """
        def game_over():
            print("game over...")
        
        def well_played():
            print(f"You found the word: {word_to_find}", 
                  "in {turn_count} turns with {error_count} errors!")