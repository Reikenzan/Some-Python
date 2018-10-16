"""What is returned when the function is invoked on the inputs below:


"""
def sum(a,b):
    return a+b

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, sum(a,b)
    return a

