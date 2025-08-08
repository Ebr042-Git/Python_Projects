import random
# Rock, Paper, Scissors Game

choices = ('r', 'p', 's')   #tuples
emojis = {                  #Dictionary for emojis 
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}   

while True:
    user_choice = input("Enter your choice (rock, paper, scissors? (r/p/s)): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please enter 'r', 'p', or 's'.")

    computer_choice = random.choice(choices)

    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")    
    elif (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 'p' and computer_choice == 'r') or \
        (user_choice == 's' and computer_choice == 'p'):       
        print("You win! 🎉")
    else:
        print("You lose! 😢")

    Play_again = input("Do you want to play again? (y/n): ").lower()
    if Play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break

