from tkinter import Canvas, Frame, Scrollbar, VERTICAL, HORIZONTAL, RIGHT, LEFT, BOTTOM, TOP, X, Y, BOTH
from tkinter import Tk, Button, Label, Entry, StringVar


def animate_text():
    global x_pos
    canvas.move(title_text, 2, 0) # Move right
    x_pos += 2
    if x_pos < 300:
        root.after(20, animate_text) # Repeat animation

root = Tk()
root.title("Title Screen Animation")
canvas = Canvas(root, width=500, height=300, bg="black")
canvas.pack()

x_pos = 50
title_text = canvas.create_text(x_pos, 150, text="My Game", font=("Arial", 40), fill="white")

animate_text()
root.mainloop()