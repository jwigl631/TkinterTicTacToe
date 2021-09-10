#Jayden Wigley
#TKinter Tic Tac Toe Project
#9/9/21
from tkinter import *
import random
root = Tk()
root.title('Tic Tac Toe')
root.geometry(500, 500)

turns = 0
buttonlist = []
size = 0

def board(size, buttonlist,number):
    clearWindow()
    number = int(number.get())
    buttonlist = [[] for i in range(number)]
    for row in range(number):
        for column in range(number):
            buttonlist[row].append(Button(root,text='-',width=12, height=4))
            buttonlist[row][column]
            buttonlist[row][column].grid(row=row+1,column=column)

number = StringVar()
sim = Button(root, command=lambda: board(size,buttonlist,number),text="Submit").grid(row=0,column=0)
label = Entry(root, textvariable=number).grid(row=1,column=0)

def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()


root.mainloop()