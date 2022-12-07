import random
import sys
from termcolor import colored

def instructions():
    print("Welcome to Wordle!\n")
    print("INSTRUCTIONS:")
    print("You have to guess the Wordle in six goes or less")
    print("Every word you enter must be in the word list." )
    print("A correct letter turns green")
    print("A correct letter in the wrong place turns yellow")
    print("An incorrect letter turns gray")
    print("Letters can be used more than once")
    print("Answers are never plurals\n")

def choose_wordle():
    with open("words.txt","r") as f:
        file = f.read()
        word_list = file.split(" ")
        wordle = random.choice(word_list)
        return wordle.upper()

def validate_guess():
    valid_word = ""
    while valid_word != "true":
        guess = input("Enter a five-letter word: ")
        if len(guess) == 5:
            valid_word = "true"
            return guess.upper()
        else:
            print("Error - word must be five letters")
            valid_word = "false"



def create_arr(word):
    array = []
    for letter in word:
        array.append(letter)
    return array

def create_dict(list):
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else: 
            dict[item] = 1
    return dict

def play_wordle():
    # Generate Wordle
    word = choose_wordle()
    wordle_arr = create_arr(word)
    wordle_dict = create_dict(wordle_arr)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    green = []
    yellow = []
    guessed = []

    turn = 1
    win = ""
    instructions()
    while turn in range(1, 7):
        # Prompt user for guess, validate guess
        print(f"Turn {turn}: ", end="")
        guess = validate_guess()
        guess_arr = create_arr(guess)

        # Evaluate guess
        i = 0
        for letter in guess:
            guessed.append(letter)
            if letter == word[i]:
                green.append(letter)
            elif letter in word:
                yellow.append(letter)
            i += 1
        # Print word to string
        for letter in guess:
            if letter in green:
                if wordle_dict[letter] > 1 and (wordle_arr.index(letter) == guess_arr.index(letter)):
                    print(colored(letter.upper(), 'grey', 'on_green'), end="")
                elif wordle_dict[letter] == 1:
                    print(colored(letter.upper(), 'grey', 'on_green'), end="")
            elif letter in yellow:
                print(colored(letter.upper(), 'grey', 'on_yellow'), end="")
            else:
                print(letter.upper(), end="")
        print("\n")
        # Create "keyboard"
        for letter in letters:
            if letter in green:
                print(colored(letter.upper(), 'grey', 'on_green'), end=" ")
            elif letter in yellow:
                print(colored(letter.upper(), 'grey', 'on_yellow'), end=" ")
            elif letter in guessed:
                print(colored(letter.upper(), 'grey', 'on_white'), end=" ")
            else:
                print(letter.upper(), end=" ")
        print("\n")
        
        if guess == word:
            print("\n")
            print(f"You win! The word was {word}!")
            win = "true"
            break
        turn += 1
    if win != "true":
        print(f"Sorry, you lost! The word was {word}!")

play_wordle()