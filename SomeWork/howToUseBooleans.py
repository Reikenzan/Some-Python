"""Write a func called isShort() that takes a str as
its parameter & returns true if str has less than 10
charaters and false otherwise. returns a boolean value"""

def isShort(s):
    if len(s) < 10:
        return True
    else:
        return False

def main():
    userStr = input("Enter a string: ")
    ans = isShort(userStr)
    print("Short string?",ans)
if __name__ == "__main__":
    main()
