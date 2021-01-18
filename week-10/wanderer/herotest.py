import tkinter as tk
from cell import Cell
from grid import Grid


# Create the window with the Tk class
root = tk.Tk()

# Create the canvas and make it visible with pack()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()  # this makes it visible

# Loads and create image (put the image in the folder)


def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        img = tk.PhotoImage(file="gifs/hero-left.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, -72, 0)
    elif event.char == "d":
        img = tk.PhotoImage(file="gifs/hero-right.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, 72, 0)
    elif event.char == "w":
        img = tk.PhotoImage(file="gifs/hero-up.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, 0, -72)
    elif event.char == "s":
        img = tk.PhotoImage(file="gifs/hero-down.gif")
        image = canvas.create_image(360, 360, anchor=tk.NW, image=img)
        canvas.move(image, 0, 72)



img = tk.PhotoImage(file="gifs/hero-down.gif")
image = canvas.create_image(360, 360, anchor=tk.NW, image=img)

# This bind window to keys so that move is called when you press a key
root.bind("<Key>", move)

# this creates the loop that makes the window stay 'active'
root.mainloop()