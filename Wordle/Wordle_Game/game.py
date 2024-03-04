import random
import solver
from colorama import Fore, Style

fin = open("input.in")

cuvinte = [x[:-1] for x in fin.readlines()]
fin.close()
cuvinte.pop()

def game_mode():
    x = input("Alege modul de joc, tastand: Manual sau Automat\n")
    if(x == "Manual"):
        return 1
    return 0

def get_feedback(guess, secret):
    feedback = ""
    for i in range(5):
        letter = guess[i]
        if letter == secret[i]:
            feedback = feedback + "V"
        elif letter in secret:
            feedback = feedback + "G"
        else:
            feedback = feedback + "N"
    return feedback

def print_feedback(feedback, guess):
    for i in range(5):
        if feedback[i] == "V":
            print(Fore.GREEN + guess[i], end='')
        elif feedback[i] == "G":
            print(Fore.YELLOW + guess[i], end='')
        else:
            print(Fore.LIGHTBLACK_EX + guess[i], end='')
    print(Style.RESET_ALL)
    return

def valid_guess(guess):
    if guess not in cuvinte:
        return 0
    return 1

def Guess():
    guess = input("Guess-ul tau este: ")
    while (valid_guess(guess) == 0):
        print("Cuvantul nu este valid")
        guess = input("Guess-ul tau este: ")
    return guess

def Session(cuvinte):
    secret_word = random.choice(cuvinte)
    if mod == 1:
        guess = Guess()
    else:
        guess = "TAREI"
    feedback = get_feedback(guess, secret_word)
    while feedback != "VVVVV":
        print_feedback(feedback, guess)
        cuvinte = solver.update_list(cuvinte, feedback, guess).copy()
        if mod == 1:
            guess = Guess()
        else:
            guess = solver.getBestWord(cuvinte)
        feedback = get_feedback(guess, secret_word)
    print_feedback(feedback, guess)
    print("Felicitari, cuvantul era " + secret_word)

mod = game_mode()
Session(cuvinte)