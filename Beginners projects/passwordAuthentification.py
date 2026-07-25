import getpass
userDataBase = {"John Doe":"Qwerty.123","Jane Doe":"Xen0ph0n"}
username = input("Please enter your username: ")
password = getpass.getpass("Please enter your password: ")
try:
    if userDataBase[username] == password:
        print("Access granted")
    else:
        print("Access denied, invalid password")
except:
    print("Access denied, invalid username")