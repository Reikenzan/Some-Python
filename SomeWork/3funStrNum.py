# write 3 functions
# 1.) no input parameter, print "hello!"
# 2.) number + 5
# 3.) prints String and does not return anything

def printHello():
    return "Hello!"

x = printHello
print("printHello() returned",x)
# 2.)
def add5(y):
    # y = y+5
    return y+5

output = add5(2)
print("add5(2) returned",output)
# 3.)
def printToScreen(string):
    print(string)

printToScreen("This is a function")
