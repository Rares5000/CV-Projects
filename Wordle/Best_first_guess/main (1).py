import math

fin = open("input.in")
fout = open("entropy.out", "w")


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


cuvinte = [x[:-1] for x in fin.readlines()]
cuvinte.pop()
lung = len(cuvinte)
cuvbun = ""
maxim = -1
patterns = []

for guess_word in cuvinte:
    entropy = 0
    f = {}
    for secret_word in cuvinte:
        feedback = get_feedback(guess_word, secret_word)
        if feedback in f:
            f[feedback] += 1
        else:
            f[feedback] = 1
    for key, value in f.items():
        prob1 = value / 11454
        entropy = entropy + (prob1 * -math.log2(prob1))
    fout.write(guess_word + " " + str(entropy) + "\n")
    if entropy > maxim:
        maxim = entropy
        cuvbun = guess_word

fout.write("Cuvantul cu cea mai mare entropie este: " + cuvbun + " " + str(entropy))