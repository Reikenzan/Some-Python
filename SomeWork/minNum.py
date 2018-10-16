# function that returns the minimun of 3 numbers

def min(num1,num2,num3):
    if num1 < num2 and num1 < num3:#check num1
        return num1
    if num2 < num1 and num2 < num3:#check num2
        return num2
    if num3 < num1 and num3 < num2:#check num3
        return num3
    return 0


def main():
    print("Start")
    n1 = 5
    n2 = 9
    n3 = 10
    minNum = min(n1,n2,n3)
    print("The min is", minNum)
if __name__ == "__main__":
    main()
