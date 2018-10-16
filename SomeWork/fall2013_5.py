"""What is returned when the function foo() is invoked on the inputs below?
(a) foo( [2, 4, 6, 8] )
(b) foo( [4002, 328, 457, 1] )


"""

def kuwae( inLst ):
    tot = 1
    for item in inLst:
        tot = tot * item
        return tot

def foo( inLst ):
    if (inLst[-1] > inLst[0]):
        return kuwae( inLst )
    else:
        return -1

foo( [2, 4, 6, 8] )
