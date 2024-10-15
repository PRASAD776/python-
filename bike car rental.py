print("welcome to our application")
print('''choose the vehicle
      1.CAR
      2.BIKE ''')
ch=int(input())
if ch==1:
    print('''choose the car
          1.AUDI
          2.BMW
          3.ALTO 800
          4.OMNI''')
    car=int(input())
    if car==1:
        print("NO OF DAYS YOU WANNA BOOK A CAR")
        days=int(input())
        print("------------------------")
        print("CAR:AUDI")
        print("NO OF DAYS:",days )
        print("TOTAL AMOUNT:",days*1500)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    elif car==2:
        print("NO OF DAYS YOU WANNA BOOK A CAR")
        days=int(input())
        print("------------------------")
        print("CAR:BMW")
        print("NO OF DAYS:",days )
        print("TOTAL AMOUNT:",days*1500)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    elif car==3:
        print("NO OF DAYS YOU WANNA BOOK A CAR")
        days=int(input())
        print("------------------------")
        print("CAR:ALTO 800")
        print("NO OF DAYS:",days )
        print("TOTAL AMOUNT:",days*800)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    elif car==4:
        print("NO OF DAYS YOU WANNA BOOK A CAR")
        days=int(input())
        print("------------------------")
        print("CAR:OMNI")
        print("NO OF DAYS:",days )
        print("TOTAL AMOUNT:",days*800)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    else:
        print("invalid choice")
elif ch==2:
    print('''choose a Bike
          1.YAMAHA MT 15
          2.YAMAHA FZ
          3.NTORQ SCOOTER
          4.APRILIA SCOOTER''') 
    bike=int(input())   
    if bike==1:
        print("No of days you wanna book a bike") 
        dayss=int(input()) 
        print("------------------------")
        print("BIKE:YAMAHA MT 15")
        print("NO OF DAYS:",dayss )
        print("TOTAL AMOUNT:",dayss*800)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    elif bike==2:
        print("No of days you wanna book a bike") 
        dayss=int(input()) 
        print("------------------------")
        print("BIKE:YAMAHA FZ")
        print("NO OF DAYS:",dayss )
        print("TOTAL AMOUNT:",dayss*800)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    elif bike==3:
        print("No of days you wanna book a scooty") 
        dayss=int(input()) 
        print("------------------------")
        print("SCOOTER:NTORQ SCOOTY")
        print("NO OF DAYS:",dayss )
        print("TOTAL AMOUNT:",dayss*500)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
    elif bike==4:
        print("No of days you wanna book a scooty") 
        dayss=int(input()) 
        print("------------------------")
        print("SCOOTER:APRILIA SCOOTY")
        print("NO OF DAYS:",dayss )
        print("TOTAL AMOUNT:",dayss*800)
        print("------------------------")
        print("THANK YOU YOUR BOOKING IS SUCCESSFULLY DONE")
else:
    print("invalid choice")
    


