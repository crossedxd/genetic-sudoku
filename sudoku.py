import math

class Sudoku:

    SIZE = 9
    BOX_SIZE = int(math.sqrt(SIZE))

    def __init__(self, grid=None):
        ''' Initializes the grid with the grid provided, otherwise with zeroes. '''
        if grid:
            self.grid = grid
        else:
            self.grid = [[0] * self.SIZE] * self.SIZE

    def get_row(self, row):
        ''' Returns the values of a given row in the grid. '''
        return [self.get_cell(row, col) for col in range(self.SIZE)]

    def get_column(self, col):
        ''' Returns the values of a given column in the grid. '''
        return [self.get_cell(row, col) for row in range(self.SIZE)]

    def get_box_containing(self, row, col):
        ''' Returns the values of the box containing cell(row, col) in the grid. '''
        box_row = math.floor(row / self.BOX_SIZE) * self.BOX_SIZE
        box_col = math.floor(col / self.BOX_SIZE) * self.BOX_SIZE
        box = []
        for sub_row in range(box_row, box_row + self.BOX_SIZE):
            for sub_col in range(box_col, box_col + self.BOX_SIZE):
                box.append(self.get_cell(sub_row, sub_col))
        return box

    def get_cell(self, row, col):
        ''' Returns the value in the grid at (row, col) coordinates. '''
        return self.grid[row][col]

    def get_string(self):
        ''' Returns the grid as a single row in string form. '''
        return ''.join([''.join(map(str, i)) for i in self.grid])
