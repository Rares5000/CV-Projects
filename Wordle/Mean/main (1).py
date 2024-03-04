import math
import time

start_time = time.time()

f = open("input.in", "r")
out = open("solutii.txt", "w")

words = [x[:-1] for x in f.readlines()]
words.pop()

def get_pattern(guess, secret):
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


def update_list(cuvinte, feedback, guess):
    cuvinte1 = cuvinte.copy()
    for x in cuvinte:
        for i in range(5):
            if feedback[i] == "N" and guess[i] in x:
                cuvinte1.remove(x)
                break
            elif feedback[i] == "G" and guess[i] not in x:
                cuvinte1.remove(x)
                break
            elif feedback[i] == "G" and guess[i] == x[i]:
                cuvinte1.remove(x)
                break
            elif feedback[i] == "V" and guess[i] != x[i]:
                cuvinte1.remove(x)
                break
    return cuvinte1


def getBestWord():
    cuvbun = ""
    maxim = -1
    for guess_word in words:
        entropy = 0
        # print(guess_word)
        f = {}
        for secret_word in words:
            feedback = get_pattern(guess_word, secret_word)
            if feedback in f:
                f[feedback] += 1
            else:
                f[feedback] = 1
        for key, value in f.items():
            prob1 = value / 11454
            entropy = entropy + (prob1 * -math.log2(prob1))

        if entropy > maxim:
            maxim = entropy
            cuvbun = guess_word
    return cuvbun

media = 0
cuvinte = words.copy()
for x in words:
    secret_word = x
    out.write("Cuvantul secret este: " + secret_word)
    out.write("\n")
    out.write("Guess-urile sunt: ")
    guess = 'TAREI'
    out.write("TAREI ")
    cnt = 1
    feedback = get_pattern(guess, secret_word)
    while feedback != "VVVVV":
        words = update_list(words, feedback, guess)
        guess = getBestWord()
        out.write(guess + " ")
        feedback = get_pattern(guess, secret_word)
        cnt += 1
    out.write("\n")
    media += cnt
    words = cuvinte.copy()
    out.write("\n")

media = media / 11454
out.write("Media de guess-uri este: " + str(media))
out.close()