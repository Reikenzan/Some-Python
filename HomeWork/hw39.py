"""Write a function called getLengths(..) that takes as a parameter a list of strings and returns a list containing the lengths of each of the strings.
You should also write a main method to test your function by asking the user for a list of strings, converting that input into an actual list, passing it to your function, and printing the returned list."""
"""
def getLengths(cat):
    li = ""
    for item in cat:
        re = len(item)
        li = li+ str(re)
    return li

def main():
    largo = input("Enter a list strings separated by commas:")
    total = getLengths(largo)
    print("Your new list is",total)
if __name__ == "__main__":
    main()
"""
"""
def length(n):
    r = []
    for i in n:
        r.append(len(n))
    return r
def accumulating():
    list = []
    strings = input("Please enter a list of strings(seperated by a white space): ")
    list = strings.split(" ")
    return list

def main():
  y = accumulating()
  x = length(y)
  print(x)

main()"""

b = input("Please enter a list of strings(seperated by a comma): ")
x = []
x.append(b)
x = b.split(",")
y = []
for i in x:
    i = i.strip()
    a = len(i)
    y.append(a)
print (y)
