account_balance = 5000
withdraw = int(input("Enter the amount you want to withdraw"))

if 0 >= withdraw:
    print("Invalid amount")

elif withdraw > account_balance :
    print("Insufficient balance") 
    

elif withdraw % 100 != 0:
    print("Amount must be multiple of 100")

else : 
    print("Withdrawal successful")
    print("Remaining balance :" , account_balance -  withdraw)