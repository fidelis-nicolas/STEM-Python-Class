names = []
while True:
    print("Enter 1 to view names")
    print("Enter 2 to add names")
    print("Enter 3 to delete names")
    print("Enter 4 to update names")
    print("Enter 5 to exit")

    option = int(input("Enter option: "))
    if option==1:
        if len(names)==0:
            print("No names in record for now")
        else:
            print(names)
    elif option == 2:
        while True:
            name = input("Enter name: ")
            if names.__contains__(name):
                print("name already exist")
            else:
                names.append(name)
                print("name added!!")
                break
    elif option ==3:
        while True:
            name = input("Enter the name: ")
            if names.__contains__(name):
                names.remove(name)
                print(name + " deleted!!")
                break
            else:
                print("Name does not exist!")
    elif option == 4:
        while True:
            name = input("Enter the name to be updated: ")
            if names.__contains__(name):
                index = names.index(name)
                newName = input("Enter new name: ")
                names[index] = newName
                print("Name is updated!!")
                break
            else:
                print("Name does not exist")
                continue
    else:
        break