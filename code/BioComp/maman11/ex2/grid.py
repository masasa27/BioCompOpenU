from cell import Cell
from copy import deepcopy


class Grid:
    def __init__(self, size=50, mapping=None) -> None:
        self.size = 50
        if not mapping:
            self.grid = [deepcopy([Cell() for _ in range(size)]) for _ in range(size)]
        else:
            assert len(mapping) == self.size
            for i in range(size):
                for j in range(size):
                    pass


    
    def compute(self):
        """This function calculates the next generation of the matrix
        """

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                celli, cellj = cell.get_next_location(i, j, self.size)
                self.grid[celli][cellj].update_from_cell(cell)

        self.compute_cells_state()
            

    def compute_cells_state(self):
        for row in self.grid:
            for cell in row:
                cell.compute_cell()


    def compute_cell_landscape(self):
        pass


a = Grid()
for i in range(10):
    a.compute()
a.compute()

k = a.grid[25][25].current_poluation
print(k)


