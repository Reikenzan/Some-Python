import random import * #imports random library

numSides = int(input("How many sides for the dice? "))
numTimes = int(input("How many times roll the dice? "))

for i in range(numTimes):
    #print(random.random()*50+50)#instuction to generate a random decimal num.
                              # between 0 included
    print(randrange(1,numSides+1)) #range generates an int between 1 and 6
