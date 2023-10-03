counter = 0
trials = 4
password = "fidelis"
while True:
    userPassword = input("Enter password: ")
    if password==userPassword:
        print ("Welcome to your computer")
        break
    counter +=1
    if counter >=3:
        print("This is not your computer")
        trials -=1
        print(str(trials) + " trials left")
        if trials ==0:
            print("Just get out!!!")
            break
        continue