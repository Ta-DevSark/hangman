import random
class Hangman:
    def __init__(self):
        self.possible_words = ['sunflower', 'pho','rambunctious','serendipity','miscellaneous','becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = random.choice(self.possible_words).upper()
        self.lives = 5
        self.correctly_guessed_letters = [" _ "] * len( self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count= 0
        self.error_count = 0

    def play(self):
        print("Let's play Hangman!")
        display = ' '.join(self.correctly_guessed_letters)
        print(f"Guess the word : {display}")
        victory = False
                        
        while self.lives > 0 and not victory:
            print(f"You have {self.lives} lives!")
            guess = input("Enter a letter: ").upper()

            if len(guess) > 1 or not guess.isalpha():
                print(f"{guess} is not a valid letter !")
                

            elif guess not in self.word_to_find:
                print(f"{guess} is not in the word!")
                self.wrongly_guessed_letters.append(guess)
                self.lives -= 1
                self.error_count += 1
                self.turn_count += 1
                
            else:
                print(f"{guess} is in the word!")
                for index, letter in enumerate(list(self.word_to_find)):
                    if letter == guess:
                        self.correctly_guessed_letters[index] = letter
                        self.turn_count += 1
                        if self.correctly_guessed_letters == list(self.word_to_find):
                            victory = True
    
            print(f"Correctly guessed letters : {self.correctly_guessed_letters},\nWrongly guessed letters : {self.wrongly_guessed_letters}\nLives left : {self.lives}\nErrors : {self.error_count}\nNumber of turns : {self.turn_count}")

    def start_game(self):
        self.play()
        
        if self.lives == 0:
            return self.game_over()
        else:
            return self.well_played()
    
    def game_over(self):
        print("game over...")
    
    def well_played(self):
        print(f"You found the word: {self.word_to_find}", 
                f"in {self.turn_count} turns with {self.error_count} errors!")
        
Hangman().start_game()


"""The purpose of OOP is to separate data into useful sections then be able to section off the functions that manipulate the data into methods, 
so you can control how the data is managed and also have the code in nice neat sections.

In hangman, there is no reason you would want this. You don't have individually functioning parts. 
Everything works together, don't use OOP. All it does is make the code harder to understand."""