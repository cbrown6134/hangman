# Hangman
#
# Colby Brown
# 10/20/19

import os
import random

def show_start_screen():
     print("  _          _   _       _____  _               _    _                                         _     ")
     print(" | |        | | ( )     |  __ \| |             | |  | |                                       | |    ")
     print(" | |     ___| |_|/ ___  | |__) | | __ _ _   _  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |    ")
     print(" | |    / _ \ __| / __| |  ___/| |/ _` | | | | |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |    ")
     print(" | |___|  __/ |_  \__ \ | |    | | (_| | |_| | | |  | | (_| | | | | (_| | | | | | | (_| | | | |_|    ")
     print(" |______\___|\__| |___/ |_|    |_|\__,_|\__, | |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)    ")
     print("                                         __/ |                      __/ |                            ")
     print("                                        |___/                      |___/                             ")
     print("                                                                                                     ")

def show_credits():
    print("   ___                                      ___                            ")                
    print("  / __|   __ _    _ __     ___      o O O  / _ \   __ __    ___      _ _   ")
    print("  |(_ |  / _` |  | '  \   / -_)    o      | (_) |  \ V /   / -_)    | '_|  ")
    print("  \___|  \__,_|  |_|_|_|  \___|   TS__[O]  \___/   _\_/_   \___|   _|_|_   ")
    print("_|'''''|_|'''''|_|'''''|_|'''''| {======|_|'''''|_|'''''|_|'''''|_|'''''|  ")
    print(" '`-0-0-''`-0-0-''`-0-0-''`-0-0-'./o--000''`-0-0-''`-0-0-''`-0-0-''`-0-0-' ")
    print("                                                                           ")

    
    print("by Colby B.")
    print("October 20, 2016")

def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, filename in enumerate(files):
         with open(path + "/" + filename, 'r') as f:
             print(str(i) + ") " + f.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)

    return path + "/" + files[choice]


def get_puzzle(file):
    # words = ["patriots", "train", "pencil", "computer", "castle", "mouse", "reindeer", "seastar", "peanut butter", "swimming pool", "driving licence"]

    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words)

def check(word, solved, guesses):
     for i in range(len(word)):
            if word[i] in guesses.lower() or not word[i].isalpha():
                solved = solved[:i] + word[i] + solved[i+1:]
                
     return solved

def get_guess():
    while True:
         
         guess = input("Guess a letter: ")

         one = len(guess)

         if one == 1 and guess.isalpha():
              return guess
         else:
              print("You need to enter one letter")
         

def display_board(solved, guesses, strikes):

     if strikes == 0:
          print("   _______  ")
          print(" |/      |  ")
          print(" |          ")
          print(" |          ")
          print(" |          ")
          print(" |          ")
          print(" |          ")
          print("_|___       ")
     elif strikes == 1:
          print("   _______  ")
          print(" |/      |  ")
          print(" |      (_) ")
          print(" |          ")
          print(" |          ")
          print(" |          ")
          print(" |          ")
          print("_|___       ")
     elif strikes == 2:
          print("   _______  ")
          print(" |/      |  ")
          print(" |      (_) ")
          print(" |       |  ")
          print(" |       |  ")
          print(" |          ")
          print(" |          ")
          print("_|___       ")
     elif strikes == 3:
          print("   _______  ")
          print(" |/      |  ")
          print(" |      (_) ")
          print(" |      \|  ")
          print(" |       |  ")
          print(" |          ")
          print(" |          ")
          print("_|___       ")
     elif strikes == 4:
          print("   _______  ")
          print(" |/      |  ")
          print(" |      (_) ")
          print(" |      \|/ ")
          print(" |       |  ")
          print(" |          ")
          print(" |          ")
          print("_|___       ")
     elif strikes == 5:
          print("   _______  ")
          print(" |/      |  ")
          print(" |      (_) ")
          print(" |      \|/ ")
          print(" |       |  ")
          print(" |      /   ")
          print(" |          ")
          print("_|___       ")
     else:
          print("   _______  ")
          print(" |/      |  ")
          print(" |      (_) ")
          print(" |      \|/ ")
          print(" |       |  ")
          print(" |      / \ ")
          print(" |          ")
          print("_|___       ")

     print(solved + " [" + guesses + "]")
     
def play_again():

    while True:
         answer = input("Would you like to play again?")

         if answer.lower() == 'no' or answer.lower() == 'n' or answer.lower() == 'nope':
            return False
         elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True

         print("What?!?!?! Just say say or no, please.")


def play():

    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved,guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
             strikes += 1

        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
         print("You win!")
    else:
         print("You lose!")


def main():
    show_start_screen()

    playing = True

    while playing:
         play()
         playing = play_again()
     
    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
