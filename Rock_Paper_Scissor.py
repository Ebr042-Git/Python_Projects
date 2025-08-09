import random

# Constants
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {
    ROCK: '🪨',
    PAPER: '📄',
    SCISSORS: '✂️'
}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors? (r/p/s)): ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice. Please enter r, p, or s.")

def display_results(user_choice, computer_choice):
    print(f"\nYou chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == ROCK and computer_choice == SCISSORS) or
          (user_choice == PAPER and computer_choice == ROCK) or
          (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win! 🎉")
    else:
        print("You lose! 😢")

def play_round():
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)
    display_results(user_choice, computer_choice)
    determine_winner(user_choice, computer_choice)

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_round()
        
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again == 'n':
                print("Thanks for playing! Goodbye!")
                return
            elif play_again == 'y':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play_game()