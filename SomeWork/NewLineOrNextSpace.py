"""
s = "Hello!"
for ch in s:
    print(ch)

print("Lehman",end=" ")# don't go to new line
print("College",end=" ")# put an space after printing and dont go net line
print("Bronx",end="!")# put a ! after printing Bronx and dont go next line
"""
"""
for i in range(1,101):
    print(i,end=" ")
    if i%10 == 0:
        print()
"""

for i in range(1,6): # move to next row
    for j in range(1,6): # print out a row
        print(i*j, end=" ")
    print()


