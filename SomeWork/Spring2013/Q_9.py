"""Write the python code for the algorithm below:
pow2(number)
    if number is less than or equal to 1
        return 2
    otherwise
        return 2 * pow2(number - 1)"""

def pow2(number):
    if number <= 1:
        return 2
    else:
        return 2 * pow2(number - 1)


#show output
print(pow2(1))
print(pow2(2))
print(pow2(3))
