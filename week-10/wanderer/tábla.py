from tkinter import *
from resource import Resource
from grid import Grid
from hero import Hero
from enemies import Enemy
from enemies import Boss


# Create the tk environment as usual
image_size = 72
board_size = 12
root = Tk()
canvas = Canvas(root, width=image_size * board_size, height=image_size * board_size)

# Creating a box that can draw itself in a certain position
grid = Grid(board_size)
hero = Hero(board_size)
enemy = Enemy(board_size)
boss = Boss(board_size)
background = Resource()


def on_key_press(e):
    # When the keycode is 111 (up arrow) we move the position of our box higher
    print(e.keycode)
    if e.keycode == 65:
        hero.i = hero.i - 1
    elif e.keycode == 68:
        hero.i = hero.i + 1
    elif e.keycode == 83:
        hero.j = hero.j + 1
    elif e.keycode == 87:
        hero.j = hero.j - 1
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
canvas.delete("all")
grid.draw(canvas, background, image_size)
hero.draw(canvas, background, image_size)
enemy.draw(canvas, background, image_size)
boss.draw(canvas, background, image_size)



# This bind window to keys so that move is called when you press a key

# Create a function that can be called when a key pressing happens
# Draw the box in the initial position


root.mainloop()
