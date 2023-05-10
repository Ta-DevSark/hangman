from utils.game import Hangman

while True:
    hangman = Hangman()
    hangman.start_game()

    prompt = input("Want another one Y/N?").lower()
    if prompt != 'y':
        break
