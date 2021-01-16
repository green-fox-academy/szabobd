from tkinter import *
from resource import Resource
from grid import Grid
from hero import Hero


# Create the tk environment as usual
image_size = 72
board_size = 10
root = Tk()
canvas = Canvas(root, width=image_size * board_size, height=image_size * board_size)

# Creating a box that can draw itself in a certain position
grid = Grid(board_size)
hero = Hero(board_size)
background = Resource()


# Create a function that can be called when a key pressing happens
def on_key_press(e):
    # When the keycode is 111 (up arrow) we move the position of our box higher
    print(e.keycode)
    if e.keycode == 38:
        hero.i = hero.i - 1
    elif e.keycode == 40:
        hero.i = hero.i + 1
    elif e.keycode == 39:
        hero.j = hero.j + 1
    elif e.keycode == 37:
        hero.j = hero.j - 1
        return
    print(hero.i)
    print(hero.j)
    hero.draw(canvas, background, image_size)
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position


# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()
grid.draw(canvas, background, image_size)

# Draw the box in the initial position


root.mainloop()
