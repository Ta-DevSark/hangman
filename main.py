from utils.game import Hangman

while True:
    hangman = Hangman()
    hangman.start_game()

    prompt = input("Play again Y/N?").lower()
    if prompt != 'y':
        break
