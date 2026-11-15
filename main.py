
import random

print("===== NUMBER GUESSING GAME =====")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("Congratulations! You guessed correctly.")
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")
