#quiz resolved

def getFirstLetters(myList):
    newList = []
    for string in myList:
        firstLetter = string[0]
        newList.append(firstLetter)
    return newList

def main():
    strList = input("Enter a list of strings:")
    userList = strList.split(",")
    returnedList = getFirstLetters(userList)
    print("Your new list is",returnedList)
if __name__ == "__main__":
    main()
