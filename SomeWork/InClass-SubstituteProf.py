#prog. to print all num fom a to b inclusive
"""
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
print(a)
print(b)"""
#or use
"""
a,b = eval(input("Enter the starting and ending numbers separated by comma: "))
for i in range(a, b+1):
    print(i)
"""
#2prog. to get operation like sqrt, sinPi
import math
"""
num = int(input("Please enter a number: ")) 
squareRoot = math.sqrt(num)
print(num, squareRoot)
sinOfPi = math.sin(math.pi)
"""
#prog. to compute the roots of a quadratic equa. ax^2 + bx + c = 0
a = int(input("Please enter a value fo a: ")) 
b = int(input("Please enter a value fo b: ")) 
c = int(input("Please enter a value fo c: ")) 

x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)

print("x1 = ",x1)
print("x2 = ",x2)
