#Jayden Wigley
#TKinter Tic Tac Toe Project
#9/9/21
from tkinter import *
import random
root = Tk()
root.title('Tic Tac Toe')

turns = 0
boardButtons = []
systemButtons= []
quantity = StringVar()

def board(boardButtons, quantity):
    clearWindow()
    quantity = int(quantity.get())
    boardButtons = [[] for i in range(quantity)]
    for row in range(quantity):
        for column in range(quantity):
            boardButtons[row].append(Button(root,text='-', width=12, height=4))
            boardButtons[row][column].grid(row=row+1,column=column)

def systemBoard():
    pass

def mainMenu():
    clearWindow()
    Label(root, text="Welcome To Tic Tac Toe", font='Arial').grid(row=0, column=0)
    Label(root, text="Select A Game Mode").grid(row=1, column=0)
    Button(root, text="Singleplayer", height=4, width=10, command=singlePlayerStart).grid(row=2, column=0)
    Button(root, text="Multiplayer", height=4, width=10, command=multiplayerStart).grid(row=3, column=0)

def singlePlayerStart():
    clearWindow()
    Label(root, text="Enter the board size (3, 6 or 9)", font='Arial').grid(row=0, column=1)
    Entry(root, textvariable=quantity).grid(row=1, column=1)
    Button(root, command=lambda: board(boardButtons, quantity), text="Enter").grid(row=2, column=1)
    Button(root, text="Return", command=mainMenu).grid(row=3, column=1)

def multiplayerStart():
    clearWindow()
    Label(root, text="Enter the board size (3, 6 or 9)", font='Arial').grid(row=0, column=1)
    Entry(root, textvariable=quantity).grid(row=1, column=1)
    Button(root, command=lambda: board(boardButtons, quantity), text="Enter").grid(row=2, column=1)
    Button(root, text="Return", command=mainMenu).grid(row=3, column=1)

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

mainMenu()
root.mainloop()