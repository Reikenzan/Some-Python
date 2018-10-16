# ask for a positive num & displays that many randoms num(1-100) in a list

import random

num = int(input("Enter a number:"))

for i in range(1,num+1):
    print(str(i)+".",random.randrange(1,101))
