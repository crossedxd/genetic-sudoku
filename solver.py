import math
from collections import Counter
import sudoku

class Solver:

    # Reference: https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3
    # More ref: https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_quick_guide.htm

    PENALTY_DUPLICATES = 100
    PENALTY_BLANKS = 1

    POPULATION_SIZE = 100
    CROSSOVER_RATE = 1.0
    MUTATION_RATE = 1.0
    

    def __init__(self):
        pass

    def get_initial_generation(self):
        pass

    def select_next_generation(self, population):
        '''
        From the wiki: https://en.wikipedia.org/wiki/Selection_(genetic_algorithm)
        1) Evaluate fitness of all members of the population, then normalize the fitness (divide by total fitness)
        2) Sort descending on fitness values
        3) Compute accumulated fitness values for each member
        4) 
        '''
        pass

    def perform_crossover(self, population):
        pass

    def perform_mutation(self, population):
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
