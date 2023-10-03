names = []
while True:
    print("Enter stop to cancel or")
    name = input("Enter your name: ")
    if name in names:
        print("Name already exist")
    else:
        names.append(name)
        print("Name Added")
        print(names)
