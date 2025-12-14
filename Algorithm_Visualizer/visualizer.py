from tkinter import Canvas, Frame, Scrollbar, VERTICAL, HORIZONTAL, RIGHT, LEFT, BOTTOM, TOP, X, Y, BOTH
from tkinter import Tk, Button, Label, Entry, StringVar
def calc():
    result.set(eval(entry.get()))

root = Tk()
result = StringVar()

entry = Entry(root)
entry.pack()

Button(root, text="=", command=calc).pack()
Label(root, textvariable=result).pack()

root.mainloop()
