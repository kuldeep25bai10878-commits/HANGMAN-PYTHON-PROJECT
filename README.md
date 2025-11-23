
 CLI Hangman Game in Python
A classic, text-based implementation of the popular word-guessing game "Hangman," written in pure Python. This script selects a random word from a diverse vocabulary list and challenges the user to guess it character by character before their chances run out.

 Features
Diverse Word Bank: Includes words from categories like Programming, Nature, Education, Music, and Emotions.

Random Selection: A new word is chosen every time you run the script.

Input Handling: Automatically converts all guesses to uppercase, making inputs case-insensitive.

Progress Tracking: Displays the word progress (e.g., P Y - H - N) as you guess correctly.

Lives System: You start with 8 chances. Incorrect guesses deduct a life.

Win/Loss Conditions: Clear feedback when the game is won or lost.

 Getting Started
Prerequisites
You need to have Python installed on your computer. This script uses the standard random library, so no external installations (pip install) are required.

Check if Python is installed:

Bash

python --version
Installation
Download the script file (e.g., save your code as hangman.py).

Open your terminal or command prompt.

Navigate to the folder where you saved the file.

Usage
Run the game using the following command:

Bash

python hangman.py
How to Play
Upon running the script, the game selects a secret word.

You will be prompted to: Guess a letter:

If your guess is correct:

The script reveals the position of that letter in the word.

(Note: If the letter appears multiple times, it updates all instances).

If your guess is incorrect:

You lose 1 chance.

The console displays how many chances you have left.

Winning: Reveal all letters before your chances reach 0.

Losing: If your chances hit 0, the game ends and reveals the correct word.

Example Output
Winning Scenario:

Plaintext

Guess a letter: p
P-----
P-----
Guess a letter: y
PY----
Guess a letter: t
PYT---
...
Congratulations you won!!!!
Losing Scenario:

Plaintext

Guess a letter: z
Incorrect guess
You have 7 chances left
...
Incorrect guess
You have 0 chances left
Game Over
you LosE
all the chances are exhausted
the correct word PLANET
File Structure
The project consists of a single Python script:

hangman.py: Contains the word list logic, the main game loop, and the win/loss checks.

Future Improvements
Ideas to extend this project:

[ ] Add ASCII art diagrams to visually draw the "Hangman" stick figure.

[ ] Prevent the user from guessing the same letter twice.

[ ] Add a "Play Again" loop so you don't have to restart the script manually.
