import random

def play_hangman():
    # List of words for the game
    words = ["python", "hangman", "banana", "school", "laptop", "apple", "programming", "developer", "challenge", "function"]
    secret_word = random.choice(words).lower()

    # Game state
    current_state = ["_"] * len(secret_word)
    lives = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(secret_word)} letters.")

    # Main game loop
    while "_" in current_state and lives > 0:
        print("\nCurrent word:", " ".join(current_state))
        print("Lives left:", lives)
        print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "None")

        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in secret_word:
            print("✅ Good guess!")
            # Reveal all positions of the guessed letter
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    current_state[index] = guess
        else:
            lives -= 1
            print("❌ Wrong guess!")

    # Game end
    if "_" not in current_state:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
    else:
        print("\n💀 You ran out of lives.")
        print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()

    