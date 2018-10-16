""" wirte a function called getSum() that takesin a list of nums as int & returns ther sum.
To test: ask foa list of nums using commas, convet this to a lis, pass it to a func &print"""
#convert a list of nums as into a list of ints

def convert(slist):
    nList = []
    for item in slist:
        nList.append(int(item))
    return nList

def getSum(numList):
    total = 0
    for num in numList:
        total = total + num
    return total

def main():
    strOfNums = input("Enter a lis of nums:")
    strList = strOfNums.split(",")
    print(strOfNums)
    print(strList)
    intList = convert(strList)
    print(intList)
    total = getSum(intList)
    print("total is:", total)
if __name__ == "__main__":
    main()
