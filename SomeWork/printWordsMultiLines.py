"""1.)print above not using loops (triangle form)
2.)using pattern form(1) change code to use a loop
3.)make this work for any word"""
w = "word"
word = input("Enter a word:")
#1.)
print(w[0:1])
print(w[0:2])
print(w[0:3])
print(w[0:4])
#2.)
"""
for i in range(4):
    print(w[0:i+1])
#3.)
word = input("Enter a word:")
x = len(word)
for i in range(x):
    print(word[0:i+1])
"""
#B. version upside down
print()
print(word)
for i in range(len(word)):
    print(word[:-(i+1)])

#C. same as A and B but crossed a leter
print()
print(word)
for i in range(len(word)):
    print(word[0:4]+word[0:i+1])
