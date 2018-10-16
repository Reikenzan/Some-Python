"""Write a function called titleList that takes as a parameter a list
of strings and returns a list containing each string capitalized as a
title. You should also write a main method to test your function by
asking the user for a list of strings, converting that input into an
actual list, passing it to your function, and print the returned list."""
"""
def titleList(strings):
    s=[]
    s.split(",")
    for i in s:
        s.upper() 
    strings = input("Enter a list strings separated:")
    List = strings.replace('"','').replace('[','').replace(']','').split(",")
    return List

    
    for i in List:
        m = ""
        for j in i.split():
            m += j[0].upper() + j[1:] + " "
            List.append(m.strip())
        return r

def main():
    lista= input("Enter a list strings separated by commas:")
    listy = titleList(lista)
    print("Your new list is", listy)
if __name__ == "__main__":
    main()
"""
def Strings():
  strings = input("Please enter a list of strings: ")
  List = strings.replace('"','').replace('[','').replace(']','').split(",")
  return List

def Capitalize(parameter):
  r = []
  for i in parameter:
    m = ""
    for j in i.split():
      m += j[0].upper() + j[1:] + " "
    r.append(m.rstrip())  
  return r

def main():
  y = Strings()
  x = Capitalize(y)
  print(x)

main()
