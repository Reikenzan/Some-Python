# 1.) ask user for 4 colors and store in a list
# 2.) have the turtle draw a square with those colors as the sides
# 3.) Generalize so user can enter any number of colors

import turtle
#1.)
colorList = []
color = "black"
while color != "":#3.)
    color = input("Enter a color(press Enter to finish):")
    colorList.append(color)
    
print(colorList)
#2.)
win = turtle.Screen()
tor = turtle.Turtle()

for c in colorList:
    print(c)
    tor.color(c)
    tor.forward(100)
    tor.left(75)

