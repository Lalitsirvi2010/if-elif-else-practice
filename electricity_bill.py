units = float(input("Enter the electricity used (in units)"))

if units <= 100:
    bill = units * 5
    
elif units <= 200:
    bill = units * 7
    
elif units <= 300:
    bill = units * 10
    
else:
    bill = units * 15
    
if bill > 1000:
    service_charge = 100

else :
    service_charge = 0

print("Service charges:" ,  service_charge)
print("Total bill:" , bill + service_charge)