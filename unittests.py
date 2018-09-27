import unittest
from sudoku import Sudoku


class TestSudokuMethods(unittest.TestCase):
    PARTIAL_PUZZLE = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                      [6, 0, 0, 1, 9, 5, 0, 0, 0],
                      [0, 9, 8, 0, 0, 0, 0, 6, 0],
                      [8, 0, 0, 0, 6, 0, 0, 0, 3],
                      [4, 0, 0, 8, 0, 3, 0, 0, 1],
                      [7, 0, 0, 0, 2, 0, 0, 0, 6],
                      [0, 6, 0, 0, 0, 0, 2, 8, 0],
                      [0, 0, 0, 4, 1, 9, 0, 0, 5],
                      [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    PARTIAL_SUDOKU = Sudoku(PARTIAL_PUZZLE)

    def test_get_row(self):
        """ Performs unit tests for the Sudoku.get_row() method. """
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(0), [5, 3, 0, 0, 7, 0, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(1), [6, 0, 0, 1, 9, 5, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(2), [0, 9, 8, 0, 0, 0, 0, 6, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(3), [8, 0, 0, 0, 6, 0, 0, 0, 3])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(4), [4, 0, 0, 8, 0, 3, 0, 0, 1])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(5), [7, 0, 0, 0, 2, 0, 0, 0, 6])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(6), [0, 6, 0, 0, 0, 0, 2, 8, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(7), [0, 0, 0, 4, 1, 9, 0, 0, 5])
        self.assertEqual(self.PARTIAL_SUDOKU.get_row(8), [0, 0, 0, 0, 8, 0, 0, 7, 9])

    def test_get_column(self):
        """ Performs unit tests for the Sudoku.get_column() method. """
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(0), [5, 6, 0, 8, 4, 7, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(1), [3, 0, 9, 0, 0, 0, 6, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(2), [0, 0, 8, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(3), [0, 1, 0, 0, 8, 0, 0, 4, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(4), [7, 9, 0, 6, 0, 2, 0, 1, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(5), [0, 5, 0, 0, 3, 0, 0, 9, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(6), [0, 0, 0, 0, 0, 0, 2, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(7), [0, 0, 6, 0, 0, 0, 8, 0, 7])
        self.assertEqual(self.PARTIAL_SUDOKU.get_column(8), [0, 0, 0, 3, 1, 6, 0, 5, 9])

    def test_get_box_containing(self):
        """ Performs unit tests for the Sudoku.get_box_containing() method. """
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 0), [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 1), [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 2), [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 3), [0, 7, 0, 1, 9, 5, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 4), [0, 7, 0, 1, 9, 5, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 5), [0, 7, 0, 1, 9, 5, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 6), [0, 0, 0, 0, 0, 0, 0, 6, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 7), [0, 0, 0, 0, 0, 0, 0, 6, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 8), [0, 0, 0, 0, 0, 0, 0, 6, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(0, 0), [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(1, 0), [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(2, 0), [5, 3, 0, 6, 0, 0, 0, 9, 8])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(3, 0), [8, 0, 0, 4, 0, 0, 7, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(4, 0), [8, 0, 0, 4, 0, 0, 7, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(5, 0), [8, 0, 0, 4, 0, 0, 7, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(6, 0), [0, 6, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(7, 0), [0, 6, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(self.PARTIAL_SUDOKU.get_box_containing(8, 0), [0, 6, 0, 0, 0, 0, 0, 0, 0])

    def test_get_cell(self):
        """ Performs unit tests for the Sudoku.get_cell() method. """
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 0), 5)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 1), 3)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 2), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 3), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 4), 7)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 5), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 6), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 7), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 8), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(0, 0), 5)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(1, 0), 6)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(2, 0), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(3, 0), 8)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(4, 0), 4)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(5, 0), 7)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(6, 0), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(7, 0), 0)
        self.assertEqual(self.PARTIAL_SUDOKU.get_cell(8, 0), 0)

    def test_get_string(self):
        """ Performs unit tests for the Sudoku.get_string() method. """
        self.assertEqual(self.PARTIAL_SUDOKU.get_string(), '530070000600195000098000060' +
                         '800060003400803001700020006060000280000419005000080079')

    def test_set_cell(self):
        """ Performs unit tests for the Sudoku.set_cell() method. """
        pass


if __name__ == '__main__':
    unittest.main()
