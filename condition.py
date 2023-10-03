print("Welcome")

password = 1234
name = input("Enter your name")
userPassword = input("Enter password")

if password == userPassword:

    print("Welcome " + name)
else:
    print("Incorrect password")