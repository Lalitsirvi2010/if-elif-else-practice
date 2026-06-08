attendance =  float(input("Enter your attendance: "))
if attendance < 0 :
    print("Invalid attendance.")
elif attendance > 100 :
    print("Invalid attendance.")
elif attendance >= 90 :
    print("Excellent attendance, allowed for exam.")
elif attendance >= 75 :
    print('Good attendance, allowed for exam.')
elif attendance >= 65 :
    print("Warning, improve attendance.")
elif attendance  >= 50 :
    print("Serious warning, meet teacher.")
else :
    print("Not allowed for exam.")
