# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Karpagam College of Engineering")
# Set geometry(widthxheight)
root.geometry('400x200')

# adding a label to the root window
label = Label(root, text = "Department of Mca ")
label.grid()

# function to display text when
# button is clicked
def clicked():
	label.configure(text = "Enjoy your Postgraduate ")

# button widget with red color text
# inside
btn = Button(root, text = "Click Me" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=2, row=1)

# Execute Tkinter
root.mainloop()
