import random

# Simple Hangman game
words = ["python", "code", "alpha", "internship", "project"]
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")
print("_ " * len(word))

while tries > 0:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only one valid letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Nice! That letter is in the word.")
    else:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    if all(l in guessed for l in word):
        print("\nYou guessed the word! Well done!")
        break
else:
    print("\nOut of tries. The word was:", word)
