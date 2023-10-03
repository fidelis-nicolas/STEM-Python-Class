import random

randNumber = random.randint(1,50)
counter = 5
while True:
    userGuess = int(input("Guess a number: "))
    if userGuess == randNumber:
        print("Congratulations")
        break
    counter -=1
    if counter == 0:
        print("Game over!!!")
        print("The correct number is" + str(randNumber))
        break
    if userGuess > randNumber:
        print("You guessed too high")
        print(str(counter) + " trials left")
    else:
        print("You guessed too low")
        print(str(counter) + " trials left")
