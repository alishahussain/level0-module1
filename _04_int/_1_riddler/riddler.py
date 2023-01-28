"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
import turtle
from tkinter import messagebox
from tkinter import simpledialog, Tk
window = Tk()
window.withdraw()

riddle1 = simpledialog.askstring(title='riddle', prompt='I act like a cat, I look like a cat, Yet I am not a cat. What am I?')
if riddle1 =='kitten':
    messagebox.showinfo(title='correct', message ='omg yay u got it right!!')
else:
    messagebox.showinfo(title='wrong', message='no u suck u got it wrong')

riddle2 = simpledialog.askstring(title='riddle', prompt='I am not alive, but I grow; I dont have lungs, but I need air; I dont have a mouth, but water kills me. What am I??')
if riddle1 =='fire':
    messagebox.showinfo(title='correct', message ='omg yay u got it right!!')
else:
    messagebox.showinfo(title='wrong', message='no u suck u got it wrong')

riddle3 = simpledialog.askstring(title='riddle', prompt='I make two people out of one. What am I?')
if riddle1 =='mirror':
    messagebox.showinfo(title='correct', message ='omg yay u got it right!!')
else:
    messagebox.showinfo(title='wrong', message='no u suck u got it wrong')
