# write a function that takes in a first and last name & returns
# person's initials
# handle  hypenated last names ie."Smith-Lopez"->S.L.

def initials(fn,ln):
    if ln.find("-") != -1:
        fi = fn[0] 
        l1i = ln[0] #get first init of lastname
        positionOfHipen = ln.find("-")
        l2i = ln[positionOfHipen + 1] #get second init of lastname
        return fi+"."+l1i+".-"+l2i+"."
    else:
        return fn[0]+"."+ln[0]+"."


fname = input("Enter your first name:")
lname = input("Enter your last name:")
init = initials(fname,lname).upper()
print("Your initials are", init)
