import math

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

def get_local_feedback(guess, secret):
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


def getBestWord(words):
    cuvbun = ""
    maxim = -1
    for guess_word in words:
        entropy = 0
        # print(guess_word)
        f = {}
        for secret_word in words:
            feedback = get_local_feedback(guess_word, secret_word)
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
