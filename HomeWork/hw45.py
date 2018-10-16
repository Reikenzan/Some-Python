"""Write a program that reads in sequences of numbers from a file and
displays them in a grid on a graphics screen. For this first program,
you can assume that there are 4 lines each with no more than 4 entries
per line. The entries on each line are separated by commas.
For example, if the file contains:
12,13,14,15
8,9,10,11
4,5,6,7
0,1,2,3
Hint: See TicTacToeLab1 for resizing the screen (win.setworldcoordinates
(-0.5,3.5,4.5,-1.0)) and drawing a grid. Here is pseudocode for this program:
1.  Draw a 4 x 4 grid to the screen (see 2048 Lab).
2.  Let row = 0
3.  For each line in the file:
4.      Split the line into nums
5.      For i in range(len(nums)):
6.          Move to (i,row)
7.          Write nums[i] to the graphics window
8.      row = row + 1
"""

from turtle import *

def display(num, col, row):
    pen = Turtle()
    pen.up()
    pen.goto(col,row)
    pen.down()
    pen.write(num,font=('Arial', 45, 'normal'))

def main():
    wn = Screen()           #The graphics window
    nums = [[12,13,14,15],      #The numbers to be displayed to the screen
            [8,9,10,11],
            [4,5,6,7],            
            [0,1,2,3]]
    n = len(nums)           #The number of rows
    m = len(nums[0])        #The number of columns (assumes all same length)
    wn.setworldcoordinates(-0.5,n-0.5,m,-1.0)     # Sets screen coordinates so that
                                                # the origin is in the upper left corner
    for row in range(n):        
        for col in range(m):
            display(nums[row][col], col, row) #Displays entry at (col,row)   
    
    wn.exitonclick() 
if __name__ == "__main__":
    main()
