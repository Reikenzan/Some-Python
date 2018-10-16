#1.)Write a prog that asks for a string & prints the num of a's in it(either a or A)
#2.)Modify your code so it has a function that takes in a string & returns num of a's

def countAs(user_string):
    num = user_string.count('a') + user_string.count("A")
    return num

"""
string = input("Enter a string:")
total = string.lower().count('a')
print("Your string has",total,"a's in it.")
"""
def main():
    string = input("Enter a string:")
    num = countAs(string)
    print("# of a's (both uppercase and lowercase: ", num)
if __name__ == "__main__":
    main()
