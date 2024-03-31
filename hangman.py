import random

def choose_word():
    words = ["hangman", "python", "programming", "computer", "game", "player", "guess"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    max_attempts = 6
    word = choose_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print("Incorrect guess. Attempts left:", max_attempts - attempts)
            if attempts == max_attempts:
                print("Sorry, you've run out of attempts. The word was:", word)
                break
        else:
            if "_" not in display_word(word, guessed_letters):
                print("Congratulations! You've guessed the word:", word)
                break

hangman()
