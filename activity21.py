sum = 0

tuloy = True

while tuloy == True:
    x = int(input("Please enter a number "))

    if x == 0:
        print("Loop Terminated")
        print("Total of all number is ", sum)
        break
    else:
        print("Continue loop")
        sum += x
        print("Current total is ", sum)
        continue