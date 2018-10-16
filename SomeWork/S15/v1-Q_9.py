#Second Version of Tic-Tac-Toe
from turtle import *
def setUp():
    win, tic = Screen(), Turtle()
    tic.speed(20)
    win.setworldcoordinates(-0.5,-0.5,3.5, 3.5)
    for i in range(1,3):
        tic.up()
        tic.goto(0,i)
        tic.down()
        tic.forward(3)
    tic.left(90)
    for i in range(1,3):
        tic.up()
        tic.goto(i,0)
        tic.down()
        tic.forward(3)
    tic.up()
    board = [["","",""],["","",""],["","",""]]
    return(win,tic,board)
def playGame(tic,board):
    numWinners = 0 ###ADDED
    for i in range(4):
        x,y = eval(input("Enter x, y coordinates for X’s move: "))
        tic.goto(x+.25,y+.25)
        tic.write("X",font=('Arial', 90, 'normal'))
        board[x][y] = "X"
        if checkWinner(board) == 'X': ###ADDED
            print('X won!') ###ADDED
            numWinners = numWinners + 1
        x,y = eval(input("Enter x, y coordinates for O’s move: "))
        tic.goto(x+.25,y+.25)
        tic.write("O",font=('Arial', 90, 'normal'))
        board[x][y] = "O"
        board[x][y] = "O"
        if checkWinner(board): ###ADDED
            print('O won!') ###ADDED
            numWinners = numWinners + 1 ###ADDED
    x,y = eval(input("Enter x, y coordinates for X’s move: "))
    tic.goto(x+.25,y+.25)
    tic.write("X",font=('Arial', 90, 'normal'))
    board[x][y] = "X"
    if checkWinner(board): ###ADDED
        print('X won!') ###ADDED
        numWinners = numWinners + 1 ###ADDED
def checkWinner(board):
    for x in range(3):
        if board[x][0] != "" and (board[x][0] == board[x][1] == board[x][2]):
            return(board[x][0]) #we have a non-empty row that’s identical
    for y in range(3):
        if board[0][y] != "" and (board[0][y] == board[1][y] == board[2][y]):
            return(board[0][y]) #we have a non-empty column that’s identical
    if board[0][0] != "" and (board[0][0] == board[1][1] == board[2][2]):
        return(board[0][0])
    if board[2][0] != "" and (board[2][0] == board[1][1] == board[2][0]):
        return(board[2][0])
    return("No winner")
def main():
    win,tic,board = setUp() #Set up the window and game board
    playGame(tic,board) #Ask the user for the moves and display
    print("\nThe winner is", checkWinner(board)) #Check for winner
main()
