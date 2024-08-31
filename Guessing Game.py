import random

def guessing_game():
    """A simple guessing game."""
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess the number.")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Start the game
guessing_game()
