# write a function that removes all a's in a string
# try another method
def removeAs(s):
    newS = s.replace("a","")
    newS = newS.replace("A","")
    return newS

def removeAs2(s):
    listNoAs = s.split("a")
    total = "" # accumulator
    for string in listNoAs:
        total = total+string
    return total

stri = input("Enter a string: ")
newy = removeAs(stri)
newby = removeAs2(stri)
print("Your string without a's is: ",str(newby))
