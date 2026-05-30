user_age = int(input("Enter your age "))
popcorn = input("Do you want popcorn (Y/N):")
popcorn_price = 80
if user_age < 5 :
    ticket_price = 50
    print ("Ticket fare" , ticket_price)

elif user_age < 18 :
    ticket_price = 100
    print("Ticket fare" , ticket_price)

else:
    ticket_price = 200
    print ("Ticket fare" , ticket_price)

if popcorn == "Y" or popcorn == "y" :
    print("Popcorn price" , popcorn_price)
    print("Total amount to be paid ",  ticket_price + popcorn_price)


else :
  print("Total amount to be paid " ,  ticket_price )