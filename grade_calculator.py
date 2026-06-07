maths = int(input("Enter marks scored in maths subject: "))
science = int(input("Enter marks scored in science subject: "))
english = int(input("Enter marks scored in english subject: "))
hindi = int(input("Enter marks scored in hindi subject: "))
computer = int(input("Enter marks scored in computer subject: "))

total = maths + science + english + hindi + computer
print("Total marks gained:", total)
percentage = total / 5
print("Percentage scored:", percentage, "%")

if maths < 35 or science < 35 or english < 35 or hindi < 35 or computer < 35:
    print("Fail because one subject mark is below 35")
elif percentage >= 90:
    print("GRADE A+")
elif percentage >= 80:
    print("GRADE A")
elif percentage >= 70:
    print("GRADE B")
elif percentage >= 60:
    print("GRADE C")
elif percentage >= 50:
    print("GRADE D")
else:
    print("FAIL")
