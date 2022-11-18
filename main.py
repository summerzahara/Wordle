import random
import sys
from termcolor import colored, cprint


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

def play_wordle():
    word = choose_wordle()
    turn = 1
    win = ""
    print("Welcome to Wordle!\n")
    while turn in range(1, 7):
        guess = validate_guess()
        i = 0
        for letter in guess:
            if letter == word[i]:
                print(colored("[{}]".format(letter.upper()), 'green'), end="")
                #print(colored(letter.upper(), 'green'), end="")
                #print(colored(letter.upper(), 'grey', 'on_green'), end="")
            elif letter in word:
                print(colored("({})".format(letter.upper()), 'yellow'), end="")
                #print(colored(letter.upper(), 'yellow'), end="")
                #print(colored(letter.upper(), 'grey', "on_yellow"), end="")
            else:
                print(letter.upper(), end="")
            i += 1
        if guess == word:
            print("\n")
            print("You win! The word was {}!".format(word))
            win = "true"
            break
        turn += 1
        print("\n")
    if win != "true":
        print("Sorry, you lost! The word was {}!".format(word))

play_wordle()