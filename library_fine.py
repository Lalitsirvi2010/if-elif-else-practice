days_late = int(input("Enter the number of days book is late: "))
member =  input("Are you a library member (Yes/No): ").lower() .strip()
valid_member = ["yes" , 'y' , 'n','no']
if member not in valid_member :
    print('Please enter valid input.')
    exit()
if days_late <= 0 :
    fine = 0
elif days_late <= 3 :
    fine = 10
elif days_late <= 7 :
    fine = 20
elif days_late <=14 :
    fine = 30
else :
    fine = 40
if member == "no" or member == "n" or days_late >14 :
    discount = 0
elif  member == "yes" or member == "y" :
    discount = 20/100
else :
    print("Please enter valid input")
    exit()
print("Fine charged: ",fine)
print("Membership discount: ",discount * fine)
print("Total fine to be paid: ", fine - (discount * fine))
