#Jayden Wigley
#TKinter Tic Tac Toe Project
#9/9/21
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

global gameBoard
turns = 0
boardButtons = []
systemButtons = []
quantity = StringVar()
mode = ""
turn = "X"

def mainMenu():
    clearWindow()
    Label(root, text="Welcome To Tic Tac Toe", font='Arial').grid(row=0, column=0)
    Label(root, text="Select A Game Mode").grid(row=1, column=0)
    Button(root, text="Singleplayer", height=3, width=10, command=boardStart).grid(row=2, column=0)
    Button(root, text="Multiplayer", height=3, width=10, command=boardStart).grid(row=3, column=0)

def boardStart():
    clearWindow()
    Label(root, text="Enter the board size (3-9)", font='Arial').grid(row=0, column=1)
    Entry(root, textvariable=quantity).grid(row=1, column=1)
    Button(root, command=lambda: board(quantity.get()), text="Enter", height=2, width=10).grid(row=2, column=1)
    Button(root, text="Return", command=mainMenu, height=2, width=10).grid(row=3, column=1)

def board(quantity):
    global gameBoard
    clearWindow()
    quantity1 = int(quantity)
    systemBoard(quantity1)

    if quantity1 % 3 == 0 and quantity1 > 0 and quantity1 < 10:
        boardButtons = [[] for i in range(quantity1)]
        for row in range(quantity1):
            for column in range(quantity1):
                boardButtons[row].append(Button(root,text=gameBoard[row][column], width=12, height=4))
                boardButtons[row][column].config(command=lambda currentrow = row, currentcolumn = column: click(currentrow, currentcolumn, quantity1))
                boardButtons[row][column].grid(row=row+1,column=column)
        if mode == "m":
            print("multi")
        elif mode == "s":
            print("single")
    else:
        messagebox.showinfo("Error", "Input a number that is a multiple of 3 between 3-9")
        boardStart()

def systemBoard(quantity1):
    global gameBoard
    gameBoard = [["" for j in range(quantity1)] for i in range(quantity1)]
    print(gameBoard)

def click(row, column, quantity1):
    global gameBoard
    gameBoard[row][column] = 'x'
    board(quantity1)

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

mainMenu()
root.mainloop()