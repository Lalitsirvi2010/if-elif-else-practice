height = float(input("Enter your height (in meters)"))
weight = float(input("Enter your weight (in kg)"))

bmi = weight / (height **2)

print("Calculated bmi" , bmi)

if bmi < 18.5 :
    print("You are underweight")

elif bmi < 25:
    print("Your weight is normal")

elif bmi < 30:
    print("You are overweight")

else:
    print("You are obese")