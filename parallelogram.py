# rows = int(input("Enter the number of rows: "))
for a in range (5):
    for b in range (5 - a -1):
        print(" ", end=" ")
    for c in range (5):
        if a == 0 or a == 5 - 1 or c == 0 or c == 5 - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    print()