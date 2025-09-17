# guessing_game.py
# A fun number guessing game using match-case statements

import random

def play_game():
    secret_number = random.randint(1, 10)  # Random number between 1 and 10
    guesses = 0
    print("🎲 I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            match guess:
                case num if num == secret_number:
                    print(f"🎉 Congratulations, you guessed it in {guesses} tries!")
                    break
                case num if num > secret_number:
                    print("📈 Oops, your guess is a bit high. Try again!")
                case num if num < secret_number:
                    print("📉 Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("⚠️ Please enter a valid number.")

while True:
    play_game()
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
