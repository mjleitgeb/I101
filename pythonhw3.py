import random

answer = 29
while True:
    guess = input("Enter a number between 1 and 100: ")
    try:
        guess = int(guess)
        if guess > answer:
            print("Too high!")
        elif guess < answer:
            print("Too low!")
        else:
            print("You guessed it!")
            break
    except:
        print("That wasn’t a number. ")

x = 0
while x < 15:
    print(x)
    x = x + 1

numList =["1" ,"2", "3", "4", "5", "6", "7", "8", "9", "10"]
while numList:
    numChoice = random.choice(numList)
    print(numList)
    numList.remove(numChoice)
