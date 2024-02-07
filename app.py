import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 5 attempts to guess it.")


    secret_number = random.randint(1, 100)
    attempts = 5

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    else:
        print(f"Sorry, you ran out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
