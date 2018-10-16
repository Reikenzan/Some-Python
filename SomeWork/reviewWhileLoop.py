"""1.) ask user for a number until they hit enter without entering
a number(empty)
   2.) at the end tell user the sum of all entered numbers"""

# ask for num
num = input("Enter a number (hit enter to stop): ")
#initialize accumulator var
total = 0
while num != "":#whil is not empty
    #add user's number to accumulaotr
    total = total + int(num)
    #ask for another number
    num = input("Enter a number (hit enter to stop): ")    
    
print("All done! The sum of all entered numbers:",str(total))

