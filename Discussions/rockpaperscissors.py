import random

choices = ['rock', 'paper', 'scissors']

while True:
    your_choice = input("rock, paper, or scissors?: ")

    while your_choice not in choices:
        print("Invalid choice. Please try again.")
        your_choice = input("Enter your choice (rock, paper, or scissors): ")

    computer_choice = random.choice(choices)

    print(f"You chose: ", your_choice)
    print(f"The computer chose: ", computer_choice)

    if your_choice == computer_choice:
        print("It's a tie!")
    elif (your_choice == 'rock' and computer_choice == 'scissors') or \
            (your_choice == 'paper' and computer_choice == 'rock') or \
            (your_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != 'yes':
        break
