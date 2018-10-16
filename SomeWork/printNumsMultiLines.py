# ask for a number and print nums in a triangle form

num = int(input("Enter a number: "))

for j in range(1,num+1):
    for i in range(1,j+1):
        print(j, end=" ")
    print()


