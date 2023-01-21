import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    px = simpledialog.askinteger(title='px', prompt='what is your radius (in pixels)?')
    
    # Make a new turtle
    lol = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    lol.circle(px)
    # Call the turtle .penup() method
    lol.penup()
    # Move your turtle to a new x,y position using .goto()
    lol.goto(100,100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    math.pi*(px**2)
    # Write the area of your circle using the turtle .write() method
    lol.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    lol.hideturtle()
    # Call turtle.done()
    turtle.done()
