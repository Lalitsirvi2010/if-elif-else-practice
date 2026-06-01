import random
valid_choice = ['Rock' , 'Paper' , 'Scissors']
computer_choice = random.choice(valid_choice)
user_choice = str(input("Select your choice (Rock , Paper , Scissors):"))
print("Computer chose:", computer_choice)

if computer_choice == "Rock" and user_choice == "Rock" :
    print("Same choice, so Draw")

elif computer_choice == "Rock" and user_choice == "Paper" :
    print("Paper over Rock YOU WON")

elif computer_choice == "Rock" and user_choice == "Scissors" :
    print("Rock breaks Scissors COMPUTER WON")

elif computer_choice == "Paper" and user_choice == "Paper" :
    print("Same choice, so Draw")

elif computer_choice == "Paper" and user_choice == "Scissors" :
    print("Scissors cuts Paper YOU WON")

elif computer_choice == "Paper" and user_choice == "Rock" :
    print("Paper over Rock COMPUTER WON")

elif computer_choice == "Scissors" and user_choice == "Scissors" :
    print("Same choice, so Draw")

elif computer_choice == "Scissors" and user_choice == "Rock" :
    print("Rock breaks Scissors YOU WON")

elif computer_choice == "Scissors" and user_choice == "Paper" :
    print("Scissors cuts Paper COMPUTER WON")

else :
    print("Please enter a valid choice")