bill = float(input("Enter total bill amount: "))
review = input("Enter your rating (Poor/Average/Good/Excellent): ").lower()
if bill > 0  :
    if review  == "poor" :
        tip = 0.05  * bill
    elif review == "average" :
        tip = 0.1 * bill
    elif review ==  "good" :
        tip = 0.15 * bill
    elif review == "excellent" :
        tip = 0.2 * bill
    else :
        print("Invalid input")
    print("Total amount to be paid" , bill  + tip , "rs")
else:
    print("Amount of bill cannot be negative or 0")
    exit()
