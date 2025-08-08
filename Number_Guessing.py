import random

number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
print("Welcome to the Number Guessing Game!")

while True: 
    try:
        guess = int(input("Enter a number between 1 and 100 for the player to guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:  
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        