from cell import Cell
import random


class Enemy:
    def __init__(self, size):
        self.grid = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                self.i = random.randint(1, 10)
                self.j = random.randint(1, 10)

                cell = Cell(self.i, self.j, "skeleton")
                row.append(cell)
            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[self.i][self.j].draw(canvas, resource, image_size)


class Boss:
    def __init__(self, size):
        self.grid = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                self.i = random.randint(1, 10)
                self.j = random.randint(1, 10)

                cell = Cell(self.i, self.j, "boss")
                row.append(cell)
            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[self.i][self.j].draw(canvas, resource, image_size)