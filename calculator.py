first_num = int(input('enter first num'))
second_num = int(input('enter second num'))
math_op = input('select operator (+ , - , * , /)')
 
if math_op == "+":
    print(first_num + second_num)     
               
elif math_op == "-": 
    print(first_num - second_num)   

elif math_op == "*":
      print(first_num * second_num)     

elif math_op == "/" :
    if second_num ==  0 :
        print("error! cannot divide by zero")
    else:
        print(first_num / second_num)

else:
    print('enter a valid operator')