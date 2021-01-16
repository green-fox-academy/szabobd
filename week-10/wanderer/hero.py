from cell import Cell


class Hero:
    def __init__(self, size):
        self.grid = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                self.i = 0
                self.j = 0
                cell = Cell(self.i, self.j, "hero_down")
                row.append(cell)
            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[self.i][self.j].draw(canvas, resource, image_size)






