import random
import string

words = ('python', 'java', 'kotlin', 'javascript')
print("H A N G M A N")


def print_state():
    global state
    state = [c if c in guesses else "-" for i, c in enumerate(word)]
    if "-" not in state:
        return True
    print("\n" + "".join(state))
    return False


def valid_guess(guess):
    if len(guess) != 1:
        print("You should input a single letter")
        return False
    elif guess not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        return False
    elif guess in guesses:
        print("You already typed this letter")
        return False
    else:
        return True


def hangman():
    global lives
    while lives > 0:
        if print_state():
            break

        letter = input("Input a letter: ")
        if not valid_guess(letter):
            continue

        guesses.add(letter)
        if letter not in word:
            lives -= 1
            print("No such letter in the word")
            continue

    if set(word) == set(state):
        print(f"You guessed the word {word}!")
        print("You survived!")
    else:
        print("You lost!\n")


while True:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == "play":
        word = random.choice(words)
        state = list("-" * len(word))
        guesses = set()
        lives = 8
        hangman()
    elif play == "exit":
        break
    else:
        continue
