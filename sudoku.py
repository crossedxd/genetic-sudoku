import math


class Sudoku:
    SIZE = 9
    BOX_SIZE = int(math.sqrt(SIZE))
    INDICES = range(SIZE)

    def __init__(self, grid=None):
        """ Initializes the grid with the grid provided, otherwise with zeroes. """
        if grid:
            self.grid = grid
        else:
            self.grid = [[0] * self.SIZE] * self.SIZE

    def get_row(self, row):
        """ Returns the values of a given row in the grid. """
        self.validate_index(row)
        return [self.grid[row][col] for col in range(self.SIZE)]

    def get_column(self, col):
        """ Returns the values of a given column in the grid. """
        self.validate_index(col)
        return [self.grid[row][col] for row in range(self.SIZE)]

    def get_box_containing(self, row, col):
        """ Returns the values of the box containing cell(row, col) in the grid. """
        self.validate_index(row)
        self.validate_index(col)
        box_row = math.floor(row / self.BOX_SIZE) * self.BOX_SIZE
        box_col = math.floor(col / self.BOX_SIZE) * self.BOX_SIZE
        box = []
        for sub_row in range(box_row, box_row + self.BOX_SIZE):
            for sub_col in range(box_col, box_col + self.BOX_SIZE):
                box.append(self.grid[sub_row][sub_col])
        return box

    def get_cell(self, row, col):
        """ Returns the value in the grid at (row, col) coordinates. """
        self.validate_index(row)
        self.validate_index(col)
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        """ Sets the value in the grid at(row, col) coordinates to the given value. """
        self.validate_index(row)
        self.validate_index(col)
        if value not in range(1, self.SIZE + 1):
            raise ValueError('value must be equal to or between %s and %s (was %s)' %
                             (min(range(1, self.SIZE + 1)), max(range(1, self.SIZE + 1)), value))
        self.grid[row][col] = value

    def get_string_repr(self):
        """ Returns the grid as a single line in string form. """
        return ''.join([''.join(map(str, i)) for i in self.grid])

    def get_as_list(self):
        """ Returns the grid as a single line in list form. """
        list_repr = []
        for row in self.grid:
            list_repr.extend(row)
        return list_repr

    def recreate_from_list(self, list_repr):
        """ Recreates the grid from a given list representation. """
        self.grid = []
        for i in range(self.SIZE):
            self.grid.append(list_repr[i * self.SIZE:i * self.SIZE + self.SIZE])

    def validate_index(self, index):
        """ Raises an IndexError if index isn't valid, i.e. doesn't fall within range(SIZE). """
        if index not in self.INDICES:
            raise IndexError('index must be equal to or between %s and %s (was %s)' %
                             (min(range(self.SIZE)), max(range(self.SIZE)), index))
