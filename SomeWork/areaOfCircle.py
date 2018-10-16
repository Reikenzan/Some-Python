import math

def welcomMessage():
    print("Welcom to my program!")
    print("It computes the area of a circle from")

def areaOfCircle(radius):
    area = radius*radius*math.pi
    return area

welcomMessage()
r = float(input("Enter a radius:"))
a = areaOfCircle(r)
print("The area of the cicle is",a)
