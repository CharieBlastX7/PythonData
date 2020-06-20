rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
orooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

def hotelroom():
    
    print("Welcome to hotel UKNWN.")
    print("Please enter building number, floor number and room number to book a room\n")
    b=int(input("Building: 0 for bldg.1, 1 for bldg.2, 2 for bldg. 3: "))
    while b>=3:
        print("There is no extra building.")
        b=int(input("Building: 0 for bldg.1, 1 for bldg.2, 2 for bldg. 3: "))
    print("\n")
    f=int(input("Floor: 0-14  "))    
    while f>=15:
        print("Sorry we don't have beyond 14 floors")
        f=int(input("Floor: 0-14  "))
    print("\n")
    t=int(input("Room 0-19: "))
    while t>=20:
        print("We don't have rooms above 20")
        t=int(input("Room 0-19: "))
            
    rooms[b][f][t]= True
    vacancy = 0
    occupied = 0
    for building in range (3):
        for floor in range (15):
            for roomNumber in range(20):
                if not rooms[building][floor][roomNumber]:
                    vacancy += 1
                else:
                    occupied+=1
                    
    print("There are",vacancy,"rooms available")
    print(occupied,"room(s) occupied.")
    print("TO LOGOUT press ctrl+c\n")
    if (occupied==900):
        print("Sorry there are no more rooms available. Please wait till someone checks out")

pwrd=input("Enter the password: ")
correct="hotelukwn"
while pwrd==correct:
    try:
        hotelroom()
    except KeyboardInterrupt:
        print("You have successfully logged out")
        break

