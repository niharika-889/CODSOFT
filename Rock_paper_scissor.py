import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_result(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def display_score(user_score, computer_score):
    print(f"\nScoreboard: You - {user_score} | Computer - {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0

    print("\nWelcome to Rock-Paper-Scissors Game!")
    print("Type 'rock', 'paper', or 'scissors'. Type 'exit' to quit.\n")

    while True:
        user_input = input("Your choice: ").lower()

        if user_input == 'exit':
            print("\nThanks for playing!")
            break

        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.\n")
            continue

        comp_choice = get_computer_choice()
        print(f"Computer chose: {comp_choice}")

        result = get_result(user_input, comp_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        display_score(user_score, computer_score)
        print("-" * 30)

play_game()