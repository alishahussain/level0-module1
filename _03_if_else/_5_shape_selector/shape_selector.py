import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # Make a new turtle
    idk = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    ask = simpledialog.askstring(title='ask', prompt='what shape would you like to draw?')
    if ask == 'circle':
        idk.circle(50)
    # Draw the shape requested by the user using if-elif-else statements
    elif ask == 'square':
        for i in range(4):
            idk.forward(100)
            idk.turn(90)
    # Call the turtle .done() method
    idk.done()
