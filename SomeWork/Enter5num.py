# ask a prog. that asks for 5 num and prints out how many are negative
count = 0
for i in range(5):
    num = int(input("Enter a number:"))
    if num < 0:
        count = count+1
        print("This number is negative")

print("The end. there were",count,"negative numbers.")
