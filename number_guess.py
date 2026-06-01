secret_num = 300
                
guess_num = int(input('Enter your guess number:'))
if guess_num == secret_num:
    print('YOU WON YOU DOMINATED THE WHOLE GAME ')
elif abs(guess_num - secret_num) < 2:
    print('You are too close ')

elif guess_num > secret_num: 
    print('You went higher, come to a low value') 
else :
    print('You went to lower value, come to a higher value')