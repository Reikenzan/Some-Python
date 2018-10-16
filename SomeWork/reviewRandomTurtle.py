# A turtle walks a random number(1-100) fordward,turns right 90^D, and repeat 50times
import turtle
import random

win = turtle.Screen()
win.bgcolor("gray")

tuty = turtle.Turtle()
tuty.color("red")
tuty.pensize(3)
tuty.speed(2)

for i in range(50):
    tuty.forward(random.randint(1,100))
    tuty.right(90)
