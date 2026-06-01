import random

computer_choice = random.choice(valid_choice)
user_choice = str(input("Select your choice (Rock , Paper , Scissors):"))

if computer_choice == "Rock" and user_choice == "Rock" :
    print("Same choice so  Draw")

elif computer_choice == "Rock" and user_choice == "Paper" :
    print("Paper over Rock YOU WONN")

elif computer_choice == "Rock" and user_choice == "Scissors" :
    print("Rock breaks Scissors COMPUTER WONN")

elif computer_choice == "Paper" and user_choice == "Paper" :
    print("Same choice so  Draw")

elif computer_choice == "Paper" and user_choice == "Scissors" :
    print("Scissors cuts Paper YOU WONN")

elif computer_choice == "Paper" and user_choice == "Rock" :
    print("Paper over Rock COMPUTER WONN")

elif computer_choice == "Scissors" and user_choice == "Scissors" :
    print("Same choice so  Draw")

elif computer_choice == "Scissors" and user_choice == "Rock" :
    print("Rock breaks Scissors YOU WONN")

elif computer_choice == "Scissors" and user_choice == "Paper" :
    print("Scissors cuts Paper COMPUTER WONN")

else :
    print("Please enter a vaild choice")