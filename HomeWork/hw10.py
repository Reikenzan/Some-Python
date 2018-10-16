import turtle
win = turtle.Screen()
tic = turtle.Turtle()
tic.speed(1)
tic.pensize(2)

win.setworldcoordinates(-10,-10,20, 20)

for i in range(0,9):
   tic.penup()
   tic.goto(0,i)
   tic.pendown()
   tic.forward(8)

tic.left(90)
for i in range(0,9):
   tic.penup()
   tic.goto(i,0)
   tic.pendown()
   tic.forward(8)

tic.penup() 

win.exitonclick()
