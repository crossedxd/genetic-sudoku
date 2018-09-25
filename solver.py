import math
from collections import Counter

class Solver:

    PENALTY_DUPLICATES = 10
    PENALTY_BLANKS = 1

    def __init__(self):
        pass

    def get_fitness(self, puzzle):
        ''' Returns the fitness of a given puzzle. '''
        fitness = 0

        total_duplicates = 0
        for i in range(puzzle.SIZE):
            total_duplicates += self.count_duplicates(puzzle.get_row(i))
            total_duplicates += self.count_duplicates(puzzle.get_column(i))
            total_duplicates += self.count_duplicates(puzzle.get_box(
                math.floor(i / puzzle.BOX_SIZE), i % puzzle.BOX_SIZE))
        fitness -= total_duplicates * self.PENALTY_DUPLICATES

        total_blanks = 0
        for i in range(puzzle.SIZE):
            total_duplicates += self.count_blanks(puzzle.get_row(i))
            total_duplicates += self.count_blanks(puzzle.get_column(i))
            total_duplicates += self.count_blanks(puzzle.get_box(
                math.floor(i / puzzle.BOX_SIZE), i % puzzle.BOX_SIZE))
        fitness -= total_blanks * self.PENALTY_BLANKS

        return fitness

    def count_duplicates(self, cells):
        ''' Returns a count of duplicate values in the given list of cells (excluding blanks). '''
        counts = Counter(cells)
        return sum([counts[i] for i in counts if counts[i] > 1 and i != 0])

    def count_blanks(self, cells):
        ''' Returns a count of blank values in the given list of cells. '''
        return sum([1 for i in cells if i == 0])
