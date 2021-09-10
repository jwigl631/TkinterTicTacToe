#Jayden Wigley
#TKinter Tic Tac Toe Project
#9/9/21
from tkinter import *
import random
root = Tk()
root.title('Tic Tac Toe')

turns = 0
buttons = []
size = 0
quantity = StringVar()

def mainMenu():
    clearWindow()
    Button(root, text="Singleplayer").grid(row=0, column=0)
    Button(root, text="Multiplayer").grid(row=0, column=0)

def start():
    Button(root, command=lambda: board(size, buttons, quantity), text="Enter").grid(row=0, column=0)
    Entry(root, textvariable=quantity).grid(row=1, column=0)

def board(size, buttons,number):
    clearWindow()
    number = int(number.get())
    buttons = [[] for i in range(number)]
    for row in range(number):
        for column in range(number):
            buttons[row].append(Button(root,text='-',width=12, height=4))
            buttons[row][column]
            buttons[row][column].grid(row=row+1,column=column)

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

start()
root.mainloop()