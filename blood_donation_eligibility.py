try:  
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (in kgs): "))
    last_donation = int(input("Days since last donation: "))
    gender = input("Enter your gender (male/female): ").lower()

    if age > 65 or age < 18 :
        print('Ineligible: Age must be between 18 and 65 years')
    elif weight < 45 :
        print("Ineligible: Weight must be at least 45 kg")
    elif last_donation < 0 :
        print("Days cannot be negative")
    elif last_donation < 90 and gender == 'male' :
        print("Ineligible: You must wait at least 90 days since your last donation.")
    elif last_donation < 120 and gender == 'female' :
        print("Ineligible: You must wait at least 120 days since your last donation.")
    elif gender != 'male' and gender != 'female' :
        print("Enter valid gender")
    else :
        print("You meet the primary age, weight, and interval criteria for blood donation in India!")
        print("Note: Final eligibility also depends on your hemoglobin levels, medical history, and vital signs on the day of donation.")

except ValueError :
     print("Invalid input. Please enter valid inputs only.")