import turtle
win = turtle.Screen()
win.bgcolor("lightgray")
tic = turtle.Turtle()
tic.speed(1)
tic.pensize(2)

win.setworldcoordinates(-0.5,-0.5,4, 4)

for i in range(0,5):
   tic.penup()
   tic.color("blue")
   tic.goto(0,i)
   tic.pendown()
   tic.forward(4)

tic.left(90)
for i in range(0,5):
   tic.penup()
   tic.color("red")
   tic.goto(i,0)
   tic.pendown()
   tic.forward(4)

tic.penup() 
#=========
for i in range(5):
   x,y = eval(input("Please enter coordinates: "))
   
   tic.goto(x+.15,y+.15)
   tic.write("2",font=('Arial', 100, 'normal'))
   tic.setx(0)
"""
   print("Please hit the enter key to continue: ")
   tic.goto(x+.25,y+.25)
   tic.write("O",font=('Arial', 90, 'normal'))
"""

win.exitonclick()
