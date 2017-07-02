import random


def getNumber(high):
    return random.randrange(1, high + 1)

print "Hello & Welcome to the Dice Rolling App"

cont = True
while cont:
    print "Your number is: " + str(getNumber(6))
    
    goodInput = False
    while not goodInput:
        cons = raw_input("Roll again? (Y/n)")
        if cons == "Y" or cons == "y":
            goodInput = True
            cont = True #superfluous
        elif cons == "N" or cons == "n":
            goodInput = True
            cont = False
        else:
            print "I don't understand."
            goodInput = False #superfluous
        


