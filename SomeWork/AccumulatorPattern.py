# Accumulator Pattern
"""
runningTotal = 0
for i in range(5):
    num = int(input("Enter a number:"))
    runningTotal = runningTotal + num
    print("So far, runningTotal is",runningTotal)

print("The sum of your numbers is", runningTotal)
"""

numOfWords = int(input("How many words do you want to enter? "))
stringSoFar = str()
numCharSoFar = 0
for i in range(numOfWords):
    word = str(input("Enter a word: "))
    stringSoFar = stringSoFar + " "+ word
    numCharSoFar = numCharSoFar + len(word)
    print("So far, stringSoFar is",stringSoFar)

print("Your sentence is", stringSoFar)
print("Your sentence has", numCharSoFar, "characters.")


