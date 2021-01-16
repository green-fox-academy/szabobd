from cell import Cell


class Grid:

    def __init__(self, size):
        self.grid = []

        for i in range(0, size):
            row = []
            for j in range(0, size):
                if i == 0 and j == 0:
                    cell = Cell(i, j, "floor")
                    row.append(cell)
                elif i % 2 == 0 and j % 2 == 0:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i % 4 == 0 and j == 3 or i == 4 and j == 1:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 5 and j % 4 == 0:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 3 and j == 6:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 2 and j == 1 or i == 2 and j == 5:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 6 and j == 7:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 7 and j == 2 or i == 7 and j == 6:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 1 and j == 6 or i == 1 and j == 8 or i == 1 and j == 9:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 8 and j == 9:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                else:
                    cell = Cell(i, j, "floor")
                    row.append(cell)

            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[i][j].draw(canvas, resource, image_size)