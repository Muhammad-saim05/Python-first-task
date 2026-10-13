import random

words = ["apple", "python", "school", "computer", "gaming"]
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Incorrect guesses left:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed this letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("Game Over! The word was:", word)