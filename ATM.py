balance = 100000
pin = 12345

print("WELCOME TO STEM BANK")
userPin = int(input("Enter your pin: "))
if pin == userPin:
    print("Enter 1 for Withdrawal")
    print("Enter 2 for Check Balance")
    print("Enter 3 for Transfer")
    print("Enter 4 for Buy Airtime")
    print("Enter 5 for Pay bills")


    #Checking user options
    userChoice = int(input("Enter choice: "))

    if userChoice == 1:
        userAmount = int(input("Enter the amount to withdraw: "))
        if userAmount <= balance:
            print("Transaction successful!!! " + str(userAmount))
        else:
            print("Insufficient fund")
    elif userChoice == 2:
        print("Your balance is: " + str(balance))
    elif userChoice == 3:
        amountToTransfer = int(input("Enter the amount: "))
        destinationBank = input("Enter destination bank: ")
        destinationAccount = input("Enter destination Account: ")

        if amountToTransfer <= balance:
            print("Amount "  + str(amountToTransfer) + " to " + destinationAccount + " " + destinationBank)

else:
    print("Incorrect pin")
