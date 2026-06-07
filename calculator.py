first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
math_op = input("Select operator (+, -, *, /): ")

if math_op == "+":
    print(first_num + second_num)
elif math_op == "-":
    print(first_num - second_num)
elif math_op == "*":
    print(first_num * second_num)
elif math_op == "/":
    if second_num == 0:
        print("Error! cannot divide by zero")
    else:
        print(first_num / second_num)
else:
    print("Enter a valid operator")
