#Jayden Wigley
#TKinter Tic Tac Toe Project
#9/9/21
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

global turn
global gameBoard
turns = 0
boardButtons = []
quantity = StringVar()
mode = ""
turn = "X"

#Main menu, choose between single player and multiplayer
def mainMenu():
    clearWindow()
    Label(root, text="Welcome To Tic Tac Toe", font='Arial').grid(row=0, column=0)
    Label(root, text="Select A Game Mode").grid(row=1, column=0)
    Button(root, text="Singleplayer", height=3, width=10, command=boardStart).grid(row=2, column=0)
    Button(root, text="Multiplayer", height=3, width=10, command=boardStart).grid(row=3, column=0)

#Where the player inputs the size of the board
def boardStart():
    clearWindow()
    Label(root, text="Enter and odd number (3-9)", font='Arial').grid(row=0, column=1)
    Entry(root, textvariable=quantity).grid(row=1, column=1)
    Button(root, command=lambda: check(quantity.get()), text="Enter", height=2, width=10).grid(row=2, column=1)
    Button(root, text="Return", command=mainMenu, height=2, width=10).grid(row=3, column=1)

#Makes sure the quantity is an odd number between 3 and 9
def check(quantity):
    quantity1 = int(quantity)
    if quantity1 % 2 == 1 and quantity1 > 1 and quantity1 < 10:
        createBoard(quantity1)
    else:
        messagebox.showinfo('Error', 'Input an odd value (3-9)')
        boardStart()

#Creates the game board arrays that store the X/O values, calls only once
def createBoard(quantity1):
    global gameBoard
    print(quantity1)
    gameBoard = [["-" for j in range(quantity1)] for i in range(quantity1)]
    print(gameBoard)
    board(quantity1)

#Displays the buttons for the boards and updates them, and switches turns
def board(quantity1):
    global gameBoard
    clearWindow()
    boardButtons = [[] for i in range(quantity1)]
    for row in range(quantity1):
        for column in range(quantity1):
            boardButtons[row].append(Button(root,text=gameBoard[row][column], width=12, height=4))
            boardButtons[row][column].config(command=lambda currentrow = row, currentcolumn = column: click(currentrow, currentcolumn, quantity1))
            boardButtons[row][column].grid(row=row+1,column=column)
    checkWinner()

#Changes button to the current turn based on which one it clicks, returns an error if the spot is taken up
def click(row, column, quantity1):
    global gameBoard
    global turn
    if gameBoard[row][column] == '-':
        gameBoard[row][column] = turn
        if turn == 'O':
            turn = 'X'
        elif turn == 'X':
            turn = 'O'
    else:
        messagebox.showinfo('Wrong Move', 'That spot has already been taken up')
    print(gameBoard)
    board(quantity1)

#Checks winner via the gameBoard array
def checkWinner():
    pass

#Clear the window
def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

mainMenu()
root.mainloop()