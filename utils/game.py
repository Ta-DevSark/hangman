import random
class Hangman():
    """"
    Here you define a class and its attributes. A class always starts with an uppercase 
    letter to distinguish it from variables and functions.
    You can call a class as a whole or function by function at the end of your code.
    """
    def __init__(self):
        """
        This is the constructor of the Hangman class. 
        It contains the attributes that you are going to use throughout the code.
        The constructor always has at least 1 parameter, "self".
        Every attribute has to refer to the class through the '.self', otherwise it becomes 
        a regular variable.
        """
        self.possible_words = ['sunflower', 'pho', 'rambunctious', 'serendipity',
                               'miscellaneous', 'becode', 'learning', 'mathematics', 'sessions',
                               'deleted', 'cautious', 'nonetheless', 'ravenous', 'pythonic']
        self.word_to_find = random.choice(self.possible_words).upper()
        self.lives = 5
        self.correctly_guessed_letters = [" _ "] * len( self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count= 0
        self.error_count = 0
        self.victory = False

    def play(self):
        """"
        This function contains the loops and conditions to make the game work.
        Again, since we are working in an OOP environment, the function takes "self" as 
        its first parameter.
        Here we use a while loop to keep the game running until the conditions are not met 
        anymore (lives> 0 and not victory).
        """        
        
        guess = input("Enter a letter: ").upper()

        if len(guess) > 1 or not guess.isalpha(): #if the input is more than 1 letter or not a letter
            print(f"{guess} is not a valid letter !")
            
        elif guess not in self.word_to_find:
            print(f"{guess} is not in the word!")
            self.wrongly_guessed_letters.append(guess)
            self.lives -= 1
            self.error_count += 1
            self.turn_count += 1
            
        else:
            print(f"{guess} is in the word!")
            self.turn_count += 1
            for index, letter in enumerate(list(self.word_to_find)):
                #this loop looks at each letter 
                #in the word the user has to find 
                #and in the next line, compares it
                #to the input guess from the user.
                if letter == guess:
                    self.correctly_guessed_letters[index] = letter
                    if self.correctly_guessed_letters == list(self.word_to_find):
                        self.victory = True

        print(f"""Correctly guessed letters : {self.correctly_guessed_letters},
        Wrongly guessed letters : {self.wrongly_guessed_letters}
        Lives left : {self.lives}
        Errors : {self.error_count}
        Number of turns : {self.turn_count}""")

    def start_game(self):
        print("Let's play Hangman!")
        print(f"You have {self.lives} lives!")
        display = ' '.join(self.correctly_guessed_letters)
        print(f"Guess the word : {display}") 

        while self.lives > 0 and not self.victory:
            self.play()
        
        if self.lives == 0:
            return self.game_over()
        else:
            return self.well_played()
    
    def game_over(self):
        print(f"game over...the correct word is {self.word_to_find}")
    
    def well_played(self):
        print(f"You found the word: {self.word_to_find}", 
                f"in {self.turn_count} turns with {self.error_count} errors!")
        
Hangman().start_game()

"""The purpose of OOP is to separate data into useful sections then be able to section 
off the functions that manipulate the data into methods, 
so you can control how the data is managed and also have the code in nice neat sections.

In hangman, there is no reason you would want this. You don't have individually functioning parts. 
Everything works together, don't use OOP. All it does is make the code harder to understand."""