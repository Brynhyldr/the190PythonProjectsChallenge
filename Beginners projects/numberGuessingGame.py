import random as rand

minNumber = 1

maxNumber = 100

x = rand.randint(minNumber,maxNumber)

lifepoint = 10

print("Welcome to Number Guessing Game!")
print("")
print("I am guessing a number between " + str(minNumber) + " and "+ str(maxNumber) +", you have " + str(lifepoint) + " chances to find it, good luck!")
print("")

while True:
    try:
        guess = int(input("Please enter your guess: "))
        if guess < minNumber or guess > maxNumber:
            print("Sorry, your entry was incorrect, please enter a valid guess...")

        elif guess > x and lifepoint > 1:
            lifepoint = lifepoint - 1
            if lifepoint > 1:
                print("Lower! Try again, you have " + str(lifepoint) + " lives left!")
            else:
                print("Lower! Try again, you have " + str(lifepoint) + " life left!")

        elif guess < x and lifepoint > 1:
            lifepoint = lifepoint - 1
            if lifepoint > 1:
                print("Higher! Try again, you have " + str(lifepoint) + " lives left!")
            else:
                print("Higher! Try again, you have " + str(lifepoint) + " life left!")

        elif guess != x and lifepoint == 1:
            print("Wrong! Sorry, you lost...")
            break

        else:
            print("Congratulations! You win!")
            break

    except:
        print("Sorry, your entry was incorrect, please enter a valid guess...")