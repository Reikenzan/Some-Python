# Complete the Turtle Racing Lab in the textbook "How To Think Like a Computer Scientist"

import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

# 5. Send them moving across the screen

andy.speed(random.randint(1,2))
lance.speed(random.randint(1,2))
andy.forward(random.randint(150,300))
lance.forward(random.randint(150,300))


wn.exitonclick()
