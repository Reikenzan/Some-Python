

def capitalizeList(li):
    newList = []
    for item in li:
        s = item + " College"
        print(s.upper())
        newList.append(s.upper())
        return newList

CUNYs = ["Lehman","Queens","Hunter","Baruch"]
newLi = capitalizeList(CUNYs)
print("my new list is",newLi)

CUNYs2 = ["Brooklyn","Staten Island"]
newLi2 = capitalizeList(CUNYs2)
print("my new list is",newLi2)
