from cell import Cell


class Grid:

    def __init__(self, size):
        self.grid = []

        for i in range(0, size):
            row = []
            for j in range(0, size):
                if i == 0 or j == 0 or i == 11 or j == 11:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 2 < i < 6 and j == 3 or 1 < j < 7 and i == 2 or i == 3 and j == 5:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 5 < j < 11 and i == 7 or 4 < i < 8 and j == 6:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 6 < i < 10 and j == 2 or 2 < j < 7 and i == 9:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif 1 < i < 6 and 7 < j < 9 or j == 9 and 6 < i < 10 or i == 3 and j == 9 or i == 5 and j == 10:
                    cell = Cell(i, j, "wall")
                    row.append(cell)
                elif i == 7 and 2 < j < 5 or i == 5 and j == 4 or i == 4 and j == 1 or i == 1 and j == 8:
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
