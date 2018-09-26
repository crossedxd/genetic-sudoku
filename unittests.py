import unittest
import sudoku

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

	BLANK_SUDOKU = Sudoku()
	PARTIAL_SUDOKU = Sudoku(PARTIAL_PUZZLE)

	def test_get_row(self):
		self.assertEqual(PARTIAL_PUZZLE.get_row(0), [5, 3, 0, 0, 7, 0, 0, 0, 0])
		self.assertEqual(PARTIAL_PUZZLE.get_row(5), [7, 0, 0, 0, 2, 0, 0, 0, 6])
		
	def test_get_column(self):
		pass
		
	def test_get_box_containing(self):
		pass
		
	def test_get_cell(self):
		pass
		
	def test_get_string(self):

if __name__ == '__main__':
	unittest.main()
