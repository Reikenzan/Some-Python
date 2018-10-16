#asks the user to enter the number of sides to
#roll a 6-sided dice. Use a function from the
#random module to simulate rolling the dice that
#manytimes and print out the sum of the rolls

import random

numD = int(input("Enter the number of dice to roll:"))
soFar = 0
for i in range(numD):
    num = random.randint(1,6)
    soFar = soFar + num
    

print("The sum of", str(numD), "dice rolls is "+ str(soFar) +".")
