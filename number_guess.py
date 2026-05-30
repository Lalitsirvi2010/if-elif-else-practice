secret_num = 300
                
guess_num = int(input('Enter your guess number'))
if guess_num == secret_num:
    print('YOU WONNNN YOU DOMINATED THE WHOLE GAME ')
elif abs(guess_num - secret_num) < 2:
    print('you are too close ')

elif guess_num > secret_num: 
    print('you gone higher come to a low value') 
else :
    print('you gone to lower value come to a higher value')