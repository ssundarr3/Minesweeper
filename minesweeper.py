# importing modules
from tkinter import *
import functools
import random
from printf import printf
import time

# Defining the number of rows and columns

# ROWS = int (input("Enter the number of rows "))
# COLS = int (input("Enter the number of cols "))
# rowTimesCol = ROWS*COLS
# MINES = int (input("Enter the number of mines "))
# if(MINES >= (0.3*rowTimesCol)):
# 	print("That's too many mines!\nResetting mines \
#         to 0.25*ROWS*COLS")
# 	MINES = int(0.25*rowTimesCol)

ROWS = 15
COLS = 10
rowTimesCol = ROWS*COLS
MINES = 25 
# minesArray is an array of size MINES
# It will contain random elements from 
# [0 to (ROWS*COLS) -1] without repeats
# range(0, n) => [0, n-1]
minesArray = random.sample(range(0, rowTimesCol), \
        MINES)
# buttons is an array of buttons...
buttons = []

# Conversion: array form to x and y coordinate form
# Array[z] = (x*ROWS) + y


def main():
    buildButtons()

def startnewGame():
    minesArray = random.sample(range(0, rowTimesCol), MINES)
    for i in range(MINES):
        printf ("%d ", minesArray[i])
    y = 0
    for row in buttons:
        x = 0
        for button in row:
            button['text'] = '?'
            button.isOpen = False
            if ((x*ROWS) + y) in minesArray:
                button.isMine = True
            else:
                button.isMine = False
            x += 1
        y += 1

def buildButtons():
    # For time
    sec = IntVar()
    timer = Label(textvariable=sec)
    timer.grid(columnspan=10, sticky=EW)
    # For game restart
    newGame = Button()
    newGame['text'] = 'New Game'
    newGame['bg'] = '#F55F55'
    newGame['command'] = startnewGame # !@!also reset timer
    newGame.grid(column=0, row=1, columnspan=COLS)    
    for y in range(ROWS):
        row = []
        for x in range(COLS):
            button = Button()
            button.grid(column=x, row=y+2)
            button['text'] = '?'
            button['bg'] = "#F55F55"
            # Add background images!!!
            # button['image'] = PhotoImage(file="hidden.png")
            button.isOpen = False
            if((x*ROWS) + y) in minesArray:
                button.isMine = True
            else:
                button.isMine = False
            command = functools.partial( \
                onButtonClick, x, y)

            # button.bind('<Button-1>', command)
            # button.bind('<Button-3>', rig)
            button['command'] = command
            row.append(button)
        buttons.append(row)


def onButtonClick(x, y): 
    button = buttons[y][x]
    if button.isOpen == True:
        return
    # Print statement that displays col and row no
    # when a button is clicked
    printf('Col (x)= %d Row (y)= %d\n', x, y)
    button.isOpen = True
    num = str(countMinesAround(x,y))
    if button.isMine == True:
        button['text'] = 'X'
    elif num == '0':
        button['text'] = ' '
        # Clicking all buttons recursively until 
        # a number is reached
        for i in range(-1, 2):
            a = i + x
            for j in range(-1, 2):
                b = j + y
                # Checking for edge cases
                if(a >= 0 and a < COLS and \
                    b >= 0 and b < ROWS):
                    onButtonClick(a, b)
    else:
        button['text'] = num

def countMinesAround(x,y):
    minesAround = 0
    for i in range(-1, 2):
        check_x = i + x
        for j in range(-1, 2):
            check_y = j + y
            if(check_x >= 0 and \
                check_x < COLS and \
                check_y >= 0 and \
                check_y < ROWS and \
                buttons[check_y][check_x].isMine):
                minesAround += 1
    return(minesAround)    

# Calling main 
root = Tk()
root.title('Minesweeper!')
main()
root.mainloop()
