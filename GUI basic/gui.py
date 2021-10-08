from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Our basic GUI")
window.geometry("400x200")
window.configure(bg="pink")

def ButtonFunc():
 messagebox.showinfo( "Love", "Python is your lover :))")

B = Button(window, text ="Click the button if you looking for a lover :)", command = ButtonFunc)
B.pack()

window.mainloop()