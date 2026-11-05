from getpass import getpass

u = "mark"
p = "123456"

isLogin = False 

while isLogin == False:

    username = input("Enter username: ")

    password = getpass("Enter password: ")

    if username == u and password == p:
        print("ACCESS GRANTED")
        isLogin = True
    else:
        print("ACCESS DENIED")
        isLogin = False