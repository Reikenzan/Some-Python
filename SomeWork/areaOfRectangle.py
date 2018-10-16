#Write a function that computes the area of a rectangle from Length and Width

def areaOfRec(length,width):
    area = length*width
    return area

RL = float(input("Enter the length:"))
RW = float(input("Enter the width:"))
a = areaOfRec(RL,RW)
print("The area of the rectangle is",a)
