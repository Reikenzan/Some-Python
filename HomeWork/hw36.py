"""Write a program that asks the user to enter a list of things to do,
with the tasks separated by commas (","). Your program should then print
out the tasks in a numbered list."""


names=input("Enter a list of things to do (separated by commas):")

listnames = names.split(",")
""" http://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3
#listy = names.split(",")
#for i in listy:
#    print(i,listy.strip())

for item in listnames:
    for i in range(names):
        print(i,item)

num = int(len(listnames) + 1
for i in range(len(listnames))
    for item in names:
        print(str(i)+".", names[i])
"""

listnames.insert(0, "zero")
num = int(len(names)) + 1
#for i in range(1,num):
#    print(str(i)+".", listnames[i])



