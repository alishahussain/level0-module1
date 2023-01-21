# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num = simpledialog.askinteger(title='num', prompt='what do u want your radius to be (in pixels)?')
    answer = simpledialog.askstring(title='answer', prompt='do u wanna calculate the area or circumfrence of a circle?')
    bob = turtle.Turtle()
    bob.circle(num)
    bob.penup()
    bob.goto(100,100)
    if answer == 'area':
        area = math.pi*(num**2)
        bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial',15,'normal'))
    elif answer == 'circumfrence':
        circum = math.pi*(2*num)
        bob.write(arg="area = " + str(circum), move=True, align='left', font=('Arial',15,'normal'))
    bob.hideturtle()
    turtle.done()
#Area = πr^2
#Circumference = 2πr 
