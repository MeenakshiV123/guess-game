import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 10  # Set the maximum number of attempts

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it correctly.\n")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed it right in {attempt} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    else:
        print(f"\nSorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

# Run the game
guess_the_number()
