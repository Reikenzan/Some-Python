
def fullname(Fname,Lname):
    fuly = len(Fname)+len(Lname)
    return fuly


Fn = input("Enter your First name:")
Ln = input("Enter your Last name:")
Full = fullname(Fn,Ln)
print("Your full name has", Full, "characters in it.")


