### Project Overview:

This project encompasses the development of a Wordle game along with its corresponding solver, an average attempts calculator, and the precomputation of the best word as the initial guess.

Within the **Wordle_Game** directory, you'll find the `game` and `solver` files, which embody the game mechanics and the algorithm responsible for making optimal guesses. To execute the program, it's essential to have the Colorama module installed. For users of VS Code, simply input the command `pip install colorama` into the terminal (assuming the Python extension for VS Code is present). For PyCharm users, we've provided guidance via the following link: [How to Install Colorama in Python](https://blog.finxter.com/how-to-install-colorama-in-python/).

The program offers two modes of gameplay: automatic (where the computer plays) or manual (where the user plays). The **Best_First_Guess** directory contains a program that calculates and logs the entropy of all initial words into `entropy.out`, subsequently selecting the word with the highest entropy. The **Calcul_medie** directory initiates by utilizing the word "TAREI" as the best first guess, followed by the continual use of the algorithm employed in **Best_First_Guess** for the updated word list. In the `solutii.txt` file, you'll discover the attempts required to guess each word in the list, culminating in the display of the average attempts.

Average attempts: 4.372882835690588
