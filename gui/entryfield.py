from tkinter import *

root = Tk()

# input fields
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    hello = "hello " + e.get()
    nameTag = Label(root, text=hello)
    nameTag.pack()


myButton = Button(root, text="enter your name", command=myClick)
myButton.pack()

root.mainloop()
