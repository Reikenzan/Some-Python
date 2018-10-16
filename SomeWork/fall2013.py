""" What is the exact output of the following?
OUTPUT:
I have 4 good friends:
Torvalds, Jobs, Gates, Python
My favorite friend is Linus
who invented LINUX
"""

my_friends = "Linus Torvalds,Steve Jobs,Bill Gates,Monty Python"
friends_list = my_friends.split(",")
count = len(friends_list)
favorite = friends_list[0].split(" ")
what = favorite[0].replace("s","x")
l_names = ""
for f in friends_list:
    l_names = l_names + ", " + f.split(" ")[-1]
print("I have", count, "good friends:")
print(l_names.strip(", "))
print("My favorite friend is", favorite[0])
print("who invented", what.upper())
