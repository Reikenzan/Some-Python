"""write a function that takes in a list of words and returns
a list of only those words with 5 letters or more"""

def getLargeWords(li):
    listIndex = 0
    while listIndex < len(li):
        word = li[listIndex]
        print(word)
        if len(word) < 5:
            li.remove(word)
        else:
            listIndex = listIndex + 1
    return li

def main():
    myList = ['cat','dog','elephant','squirrel']
    newList = getLargeWords(myList)
    print("Long words are:"+str(newList))
if __name__ == "__main__":
    main()
