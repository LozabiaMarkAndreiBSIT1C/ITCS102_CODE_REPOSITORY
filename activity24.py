#JEEPNEY SIMULATOR 
route = ["Terminal", 'Perez park', "Pacific Mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0 

while True:
    print()
    print("Sakay", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 sakay 2 Priority seat 3 Para po!")
    print("4 Baba po sa kanto 5 Baba sa harap ")
    print("Seat check  7 Balikan 8 Exit")
    choice = input("choice :")

    if choice == "1":
        if len(passengers) == SEATS:
            print("PUno na!")
        else:
            name = input("Name:")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the back")
    elif choice == "2":
        if len(passengers) == SEATS:
            print("Puno na!")
        else:
            name = input("Name:")
            passengers.insert(0, name)
            total = total + FARE 
            print(name, "took the priority seat")
    elif choice == "3":
        name = input("Who is getting off?")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. Ingat!")
        else:
            print(name, "is not on this jeep.")
    elif choice == "4":
        if len(passengers) == 0:
            print("The jeep is empty.")
        else:
            left = passengers.pop()
            print(left,"got off the door")
    elif choice == '5':
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            front = passengers.pop()
            print(front, "got off the front.")
    elif choice == "6":
        for i in range(len(passengers)):
            print("seat", i + 1, passengers [1])
    elif choice == "7":
        route.reverse()
        print("Route:", route)
    elif choice == "8":
        print("Total fare today", total)
        break
    else:
        print('Invalid Choice.')