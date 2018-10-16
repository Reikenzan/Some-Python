# funtion for turtle to draw a square
import turtle

def drawSqr():
    for i in range(4):
        tu.forward(100)
        tu.right(90)

win = turtle.Screen()
tu = turtle.Turtle()

tu.color("red")
tu.pensize(3)
tu.speed(2)

col = str(input("Enter a color:"))

drawSqr()
tu.forwadr(200)
for i in range(3):
    drawSqr()
    tu.left(90)
    tu.forwadr(100)

