import math
from collections import Counter
import sudoku

class Solver:

    PENALTY_DUPLICATES = 100
    PENALTY_BLANKS = 1

    def __init__(self):
        pass

    def get_fitness(self, puzzle):
        ''' Returns the fitness of a given puzzle. '''
        fitness = 0
        fitness -= self.count_total_duplicates(puzzle)
        fitness -= self.count_total_blanks(puzzle)
        return fitness

    def count_total_duplicates(self, puzzle):
        ''' Returns a total count of duplicate values in a given puzzle. '''
        total_duplicates = 0
        for i in range(puzzle.SIZE):
            total_duplicates += self.count_duplicates(puzzle.get_row(i))
            total_duplicates += self.count_duplicates(puzzle.get_column(i))
            total_duplicates += self.count_duplicates(puzzle.get_box_containing(
                math.floor(i / puzzle.BOX_SIZE), i % puzzle.BOX_SIZE))
        return total_duplicates * self.PENALTY_DUPLICATES

    def count_total_blanks(self, puzzle):
        ''' Returns a total count of blank values in a given puzzle. '''
        total_blanks = 0
        for i in range(puzzle.SIZE):
            total_blanks += self.count_blanks(puzzle.get_row(i))
            total_blanks += self.count_blanks(puzzle.get_column(i))
            total_blanks += self.count_blanks(puzzle.get_box_containing(
                math.floor(i / puzzle.BOX_SIZE), i % puzzle.BOX_SIZE))
        return total_blanks * self.PENALTY_BLANKS

    def count_duplicates(self, cells):
        ''' Returns a count of duplicate values in the given list of cells (excluding blanks). '''
        counts = Counter(cells)
        return sum([counts[i] for i in counts if counts[i] > 1 and i != 0])

    def count_blanks(self, cells):
        ''' Returns a count of blank values in the given list of cells. '''
        return sum([1 for i in cells if i == 0])
