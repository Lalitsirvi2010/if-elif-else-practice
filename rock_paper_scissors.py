import random

valid_choice = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(valid_choice)
user_choice = input("Select your choice (Rock, Paper, Scissors): ").strip()

print("Computer chose:", computer_choice)

if user_choice not in valid_choice:
    print("Please enter a valid choice")
elif computer_choice == user_choice:
    print("Same choice, so Draw")
elif (computer_choice == "Rock" and user_choice == "Scissors") or \
        (computer_choice == "Paper" and user_choice == "Rock") or \
        (computer_choice == "Scissors" and user_choice == "Paper"):
    print("COMPUTER WON")
else:
    print("YOU WON")
