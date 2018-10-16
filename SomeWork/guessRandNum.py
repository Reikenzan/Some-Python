""" pick a random num from (1-100) & ask the user to guess. tell if guess is too high or low."""
# generates random number and stores it in num
import random
ans = "y"
#loop until user doesn't want to play
while ans =="y" or ans =="yes":
    num = random.randrange(1,101)
        
    guess = 0 #initialize guess to be 0(a wrong answer)
    #loop until user guesses num:
    while guess != num:
        #-ask user to guess and store in var guess
        guess = int(input("Enter your guess:"))
        #-check if guess is too high or too low & if correct, congratulates
        if guess > num:
            print("Your guess is too high")
        elif guess < num:
            print("Your guess is too low")
        else:
            print("Congratulations! You guessed  my number.")
            
        # game has ended. Ask if want to play again
    ans = str(input("Do you want to play again(Y/N)"))
#end of loop.
print("Thanks for playing")
