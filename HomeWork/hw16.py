import turtle

def square( size ):
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(size)


num = int(input("Enter a number: "))
square(num)


