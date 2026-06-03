driver_name = str(input("Enter the driver's name: "))
vehicle_type = str(input("Enter the type of vehicle (car, motorcycle, truck): ")).lower()
speed = int(input("Enter the speed of the vehicle (in km/h): "))
license = str(input("Does driver has a valid license? (yes/no): ")).lower()

if speed < 0:
    print("Invalid speed entered.")
    exit()

else:
    if vehicle_type == 'bike':
       speed_limit = 60 

    elif vehicle_type == 'car':
       speed_limit = 80

    elif vehicle_type == 'truck':
        speed_limit =   50

    else:
         print("Invalid vehicle type entered.")
         exit()

    if speed <= speed_limit:
        overspeeding_fine = 0 

    elif speed_limit - speed >= 10:
        overspeeding_fine = 500

    elif speed_limit - speed >= 30:
       overspeeding_fine = 1500

    else:
       overspeeding_fine = 3000

    if license == 'no':
        license_fine = 1000
    
    elif license == 'yes':
        license_fine = 0

    else:
        print("Invalid input for license status.")
        exit()

    total_fine = overspeeding_fine + license_fine

    print("TRAFFICE FINE REPORT")
    print("Driver's name :" , driver_name)
    print("Vehicle :" , vehicle_type)
    print("Speed :" , speed, "km/h")
    print("Overspeeding fine :" , overspeeding_fine, "Rs")
    print("License fine :" , license_fine, "Rs")
    print("Total fine :" , total_fine, "Rs")


