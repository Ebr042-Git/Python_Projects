import random

roll_count = 0 

while True:
    choice = input("Do you want to roll the dice? (y/n): ").strip().lower()
    if choice == 'y':
        dice_count = input("Which dice you want to roll? (Red / Blue / Both):".strip().lower())
        if dice_count == 'red':
            print("You rolled a Red Die: ", random.randint(1, 6))
            roll_count += 1
        elif dice_count == 'blue':
            print("You rolled a Blue Die: ", random.randint(1, 6))
            roll_count += 1
        elif dice_count == 'both':
            print("You rolled a Red Die: ", random.randint(1, 6))
            print("You rolled a Blue Die: ", random.randint(1, 6))
            roll_count += 2
        else:
            print("Invalid choice. Please choose 'Red', 'Blue', or 'Both'.")
    elif choice == 'n':
        print(f"Thank you for playing! You rolled the dice {roll_count} times.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")    