name = input("Input name --->"   )
age = int(input("Enter your age --->"))

print ('Hello',name, "That age is considered as")
if age >=1 and age <= 5:
    print("Infant")

elif age >= 6 and age <= 12:
    print("Child")

elif age >= 13 and age <= 19:
    print("Teenager")

elif age >= 20 and age <= 35:
    print("Young Adult")

elif age >= 36 and age <= 55:
    print("Adult")
elif age >= 56 and age <= 75:
    print("Senior Adult")

elif age >= 76 and age <= 100:
    print("Elderly")

else:
    print("Invalid age")