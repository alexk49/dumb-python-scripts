from tkinter import *

# everything is a widget

# first thing you make is the root widget
# which is basically the main window

root = Tk()

mylabel1 = Label(root, text="hello world")
mylabel2 = Label(root, text="My name is blah blah ")

# position items using grid system
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)

# numbering is relative to other items

# gray out button
myButton = Button(root, text="click me", state=DISABLED)

# resize button with padding
myButton2 = Button(root, text="click me too", padx=20, pady=20)


def myClick():
    mylabel = Label(root, text="look i clicked a button")
    mylabel.grid(column=0, row=0)


# make a button do something!
# must call a different function
# make sure not to put myClick()
# as this will run the function on load
myButton3 = Button(root, text="click me too 2", padx=20, pady=20, command=myClick)

myButton.grid(row=2, column=2)
myButton2.grid(row=3, column=2)
myButton3.grid(row=4, column=2)




root.mainloop()
