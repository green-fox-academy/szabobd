from random import shuffle, randrange
def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    for (a, b) in zip(hor, ver):
        print(''.join(a + ['\n'] + b))

make_maze()

img_d = PhotoImage(file="gifs/hero-down.gif")
image_down = canvas.create_image(72, 72, anchor=NW, image=img_d)


def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        canvas.move(image_down, -72, 0)
    elif event.char == "d":
        canvas.move(image_down, 72, 0)
    elif event.char == "w":
        canvas.move(image_down, 0, -72)
    elif event.char == "s":
        canvas.move(image_down, 0, 72)

root.bind("<Key>", move)