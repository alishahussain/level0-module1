"""
 * Write a python program that prints the word 'banana' one thousand (1,000) times
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    x = -475
    y = 390
    window = Tk()
    window.withdraw()
    minion = turtle.Turtle()
    minion.speed(0)
    minion.penup()
    minion.goto(x,y)

    for i in range(1000):
        if minion.xcor() >= 475:
            y -= 20
            minion.goto(x,y)
        else:
            minion.write(arg="banana ", move=True, align='left', font=('Arial',15,'normal'))



