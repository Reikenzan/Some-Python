"""Write a function called isExcited(...) that takes in a string and returns
i) True if the string ends with an exclamation mark or ii) False is the string
does not end with an exclamation mark. To test your function, write a main
method that asks the user for a string and prints what the function returns
(True or False) to the screen. Hint: True and False are boolean values. You
should not put quotes around them because "True" and "False" (with quotes)
are strings, not boolean values."""

def isExcited(s):
    if s == "!":
        return True
    else:
        return False

def main():
    myStr = input("Enter a string:")
    ToF = def isExcited(myStr)
    print("Your string ends with an exclamation mark:",ToF+".")

if __name__ == "__main__":
    main()
