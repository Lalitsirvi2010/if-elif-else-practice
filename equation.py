from math import sqrt

print('ax^2 + bx + c = 0')
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

if a == 0:
    print("In a quadratic equation, a cannot be 0")
else:
    d = b * b - 4 * a * c
    if d < 0:
        print("Roots are not real")
    else:
        print("Value of delta is", d)
        print()
        print("The roots are", (-b + sqrt(d)) / (2 * a), "and", (-b - sqrt(d)) / (2 * a))
