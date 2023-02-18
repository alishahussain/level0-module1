"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

import turtle
from tkinter import Tk
if __name__ == '__main__':
    x = -300
    y = 300
    window = Tk()
    window.withdraw()
    john = turtle.Turtle()
    john.penup()
    john.goto(x,y)

    for i in range(3):
        john.write(arg="ice cream ", move=True, align='left', font=('Arial',70,'normal'))
        y -= 70
        john.goto(x,y)

    y -= 70
    john.write(arg="banana ", move=True, align='left', font=('Arial',70,'normal'))



root = tk.Tk()

canvas = tk.Canvas(root, bg="#FF00FF");
canvas.grid()

root.mainloop()
