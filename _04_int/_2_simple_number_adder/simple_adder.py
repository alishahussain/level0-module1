"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
import math
import turtle
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()

hello = turtle.Turtle()
num1 = simpledialog.askinteger(title='num1', prompt='enter a number')
num2 = simpledialog.askinteger(title='num2', prompt='enter another number')
calculator = num1+num2
hello.write(arg="sum = " + str(calculator), move=True, align='left', font=('Arial',15,'normal'))
