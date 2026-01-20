#program created using if, else, elif .

print("Uber Cab Services")
name=input("Enter Your Name: ")
address=input("Enter city name you want to travel: ")
distance=int(input("Enter km: "))
book_ride=int(input("Confirm to book your ride enter (1): ")) #1 for booking ride
if book_ride==1:
    print("Ride is booked")
elif book_ride==1 and distance<=0:
    print("Sorry cant book ride!!! Distance is too low")
else:
    print("Ride cancelled")                                   #cancelling ride if user enters any number other than (1)
if distance<=0:
    print(" Distance must be greater than (0) km")
elif distance<=100:
    print(f"100 rupees for going to {address}")
    print(f"Enjoy the ride {name}")
elif distance>100 and distance<=200:
    print(f"250 rupees for going to {address}")
    print(f"Enjoy the ride {name}")
elif distance>200 and distance<=500:
    print(f"350 rupees for going to {address}")
    print(f"Enjoy the ride {name}")
elif distance>500 and distance<=800:
    print(f"500 rupees for going to {address}")
    print(f"Enjoy the ride {name}")
elif distance>800 and distance<=1000:
    print(f"Between 850 to 1000 for going to {address}")
    print(f"Enjoy the ride {name}")
else:
    print(f"Thanks for trying our services {name}")
    print("Sorry but our cab services ranges between 100 to 1000 km only")


