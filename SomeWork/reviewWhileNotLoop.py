"""ask the user if they want to play again(y/n). If user enters 'y'
or 'n' print it to the screen. If Not, tell them if was invalid &
and keep asking for a valid input until they enter 'n' or 'y'. then
print it to the screen"""

ans = input("Do you want to play again? (y/n)")
while not(ans == 'y' or ans =='n'):
    print("invalid")
print("you entered",ans)
