import random
class Hangman:
    def __init__(self, word):
        self.word = word
        self.possible_words = ['sunflower', 'pho','rambunctious','serendipity','miscellaneous','becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(word)
        self.wrongly_guessed_letters = []
        self.turn_count= 0
        self.error_count = 0

    def play(self):
        print("Let's play Hangman!")
        print(f"You have {self.lives} lives!")
        print(self.correctly_guessed_letters)
        
        while self.lives > 0:
            guess = input("Enter a letter: ").upper()
            if guess in self.word_to_find:
                print(f"{guess} is in the word!")
                new_correct_letters = ""
                for i, letter in enumerate(self.word_to_find):
                    if letter == guess:
                        new_correct_letters += letter
                    else:
                        new_correct_letters += self.correctly_guessed_letters[i]
                self.correctly_guessed_letters = new_correct_letters
                self.turn_count += 1

            elif guess not in self.word_to_find:
                print(f"{guess} is not in the word!")
                self.wrongly_guessed_letters.append(guess)
                self.lives -= 1
                self.error_count += 1
                self.turn_count += 1
                
            elif len(guess) > 1 or not guess.isalpha():
                print(f"{guess} is not a valid letter !")
            
    def start_game(self):
        self.play()
        print(f"{self.correctly_guessed_letters},\n{self.wrongly_guessed_letters},\n{self.lives},\n{self.error_count},\n{self.turn_count}")
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()

    def game_over(self):
        print("game over...")
    
    def well_played(self):
        print(f"You found the word: {self.word_to_find}", 
                f"in {self.turn_count} turns with {self.error_count} errors!")
        
Hangman("test").start_game()