try :
    vehicle_type = input("Enter your vehicle type (bike/car/truck): ").lower()
    if vehicle_type == "bike" :
        hourly_rate  =  20
    elif vehicle_type == "car" :
        hourly_rate = 50
    elif vehicle_type  == "truck" :
        hourly_rate = 100
    else :
        print("Invalid vehicle type")
        exit()

    hours = float(input("For how many hours your vehicle was parked."))
    if  hours == 0 or hours < 0 :
        print("Hours cannot be negative or 0")
        exit()
    elif hours < 8 :
        extra_charge = 0
    elif hours < 24 :
        extra_charge =  100
    else :
        extra_charge = 300
    if  hours >= 24 :
    
        overnight_charge = 200
    else :
        overnight_charge = 0
    print("Invoice")
    print("Hourly rate: ",hourly_rate)
    print("Extra charge: ",extra_charge)
    print("Overnight charge: ",overnight_charge)
    print("Total amount to be paid: ",(hourly_rate * hours) + overnight_charge + extra_charge)

except ValueError :
    print("Invalid input. Please enter valid hours.")
