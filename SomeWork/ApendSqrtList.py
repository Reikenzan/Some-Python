# write a func that takes a list of nums & returns a new lis of their squares
import math

def Squares(numList):
    squaredList = []
    for item in numList:
        print(int(item)**2)
        squaredList.append(int(item)**2)
    return squaredList

listStr = input("Enter a list of numbers separated by commas:")
nums = listStr.split(",")
print("Original list is",nums)
squaredNums = Squares(nums)
print("My squared numbers are",squaredNums)
