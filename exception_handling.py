try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter an opertor: ")
    if operator == "+":
        print(num1+num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1/num2)
except Exception:
    print("There is an error!!")
finally:
    print("Another program running")
