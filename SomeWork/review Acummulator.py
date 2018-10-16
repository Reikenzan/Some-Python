# Ask for a number, pass it into a function which computes the
# factorial and returns it to the main prog. that prints it

def factorial(num):
    total = 1
    for i in range(1,num+1):
        total = total * i        
        print("in loop: i =",i,"and total =",total)
    return total

def main():
# ask for number
    num = int(input("Enter a number:"))

# compute factorial
    factorialOf = factorial(num)

# print factorial
    print("Factorial of ",num, "is", factorialOf)

if _name_ == "_main_":
    main()
