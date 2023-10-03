studentNames = []
# print(studentNames)
# studentNames[1] = "Aseeyahtu"
# print(studentNames)


while True:
    print("Enter 1 to view Student names")
    print("Enter 2 to add Student names")
    print("Enter 3 to Delete Student names")
    print("Enter 4 to Update Student names")
    print("Enter 5 to quit")

    userOption = int(input("Enter option: "))
    if userOption == 1:
        if len(studentNames) == 0:
            print("No record found")
        else:
            print(studentNames)
    elif userOption == 2:
        while True:
            name = input("Enter student name: ")
            if name in studentNames:
                print("Name already exist")
            else:
                studentNames.append(name)
                print("Name " + name +" Added!!")
                break
    elif userOption == 3:
        while True:
            name = input("Enter name to delete: ")
            if name in studentNames:
                studentNames.remove(name)
                print("Name " + name + " deleted!!")
                break
            else:
                print("Name does not exist")
    elif userOption == 4:
        while True:
            name = input("Enter name to be updated: ")
            if name in studentNames:
                nameIndex = studentNames.index(name)
                newName = input("Enter new name: ")
                studentNames[nameIndex] = newName
                print(name + " updated!!")
                break
            else:
                print("Name does not exist! ")
    else:
        break

