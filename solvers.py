import math
import random
import pprint
import numpy
from deap import base, creator, tools, algorithms
from sudoku import Sudoku


class NaiveSolver:

    def __init__(self):
        pass

    def solve(self, puzzle: Sudoku):
        changed = True
        while changed:
            changed = False
            for row in range(puzzle.SIZE):
                for col in range(puzzle.SIZE):
                    '''
                    TODO: the naive solver needs to grab possible values for each blank in a
                    row/col/cell and then check for any numbers that only occur once.  If found,
                    they're a part of the solution.
                    '''
                    possible_values = puzzle.get_possible_values(row, col)
                    print('%s, %s: %s' % (row, col, possible_values))
                    if len(possible_values) == 1:
                        print('setting cell to %s' % (possible_values[0]))
                        puzzle.set_cell(row, col, possible_values[0])
                        changed = True
        return puzzle


class GeneticSolver:
    PENALTY_DUPLICATES = 100
    PENALTY_BLANKS = 1
    PENALTY_NO_VALUES = 100
    POPULATION_SIZE = 1000
    GENERATIONS = 100
    CROSSOVER_PROBABILITY = 0.5
    MUTATION_PROBABILITY = 0.2
    FITNESS_MODEL = Sudoku()

    def __init__(self):
        pass

    def solve(self, puzzle):
        creator.create('FitnessMax', base.Fitness, weights=(1.0,))
        creator.create('Individual', list, fitness=creator.FitnessMax)

        toolbox = base.Toolbox()
        toolbox.register('attr_val', random.randint, 0, 9)

        toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_val,
                         puzzle.SIZE ** 2)
        toolbox.register('population', tools.initRepeat, list, toolbox.individual)

        toolbox.register('evaluate', self.evaluate)
        toolbox.register('mate', tools.cxTwoPoint)
        toolbox.register('mutate', tools.mutUniformInt, low=1, up=puzzle.SIZE,
                         indpb=self.MUTATION_RATE)
        toolbox.register('select', tools.selTournament, tournsize=3)

        pop = toolbox.population(n=self.POPULATION_SIZE)
        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register('avg', numpy.mean)
        stats.register('std', numpy.std)
        stats.register('min', numpy.min)
        stats.register('max', numpy.max)

        pop, log = algorithms.eaSimple(pop, toolbox, cxpb=self.CROSSOVER_PROBABILITY,
                                       mutpb=self.MUTATION_PROBABILITY, ngen=self.GENERATIONS,
                                       stats=stats, halloffame=hof, verbose=True)

        winner = Sudoku()
        winner.recreate_from_list(hof[0])
        pprint.pprint(winner.grid)
        return pop, log, hof

    def evaluate(self, list_repr):
        """ Returns the fitness of a given puzzle. """
        self.FITNESS_MODEL.recreate_from_list(list_repr)
        fitness = 0
        fitness -= count_total_duplicates(self.FITNESS_MODEL) * self.PENALTY_DUPLICATES
        fitness -= count_total_blanks(self.FITNESS_MODEL) * self.PENALTY_BLANKS
        for row in range(self.FITNESS_MODEL.SIZE):
            for col in range(self.FITNESS_MODEL.SIZE):
                if self.FITNESS_MODEL.get_cell(row, col) == 0:
                    fitness -= self.PENALTY_BLANKS
                    if not self.FITNESS_MODEL.get_possible_values(row, col):
                        fitness -= self.PENALTY_NO_VALUES
        return fitness,


def count_total_duplicates(puzzle):
    """ Returns a total count of duplicate values in a given puzzle. """
    total_duplicates = 0
    for i in range(puzzle.SIZE):
        total_duplicates += count_duplicates(puzzle.get_row(i))
        total_duplicates += count_duplicates(puzzle.get_column(i))
        total_duplicates += count_duplicates(puzzle.get_box_containing(
            math.floor(i / puzzle.BOX_SIZE) * puzzle.BOX_SIZE,
            i % puzzle.BOX_SIZE * puzzle.BOX_SIZE))
    return total_duplicates


def count_total_blanks(puzzle):
    """ Returns a total count of blank values in a given puzzle. """
    return sum([count_blanks(puzzle.get_row(i)) for i in range(puzzle.SIZE)])


def count_duplicates(cells):
    """ Returns a count of duplicate values in the given list of cells (excluding blanks). """
    excluding_blanks = [i for i in cells if i != 0]
    return len(excluding_blanks) - len(set(excluding_blanks))


def count_blanks(cells):
    """ Returns a count of blank values in the given list of cells. """
    return sum([1 for i in cells if i == 0])
