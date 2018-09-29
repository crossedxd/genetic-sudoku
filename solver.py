import math
import random
import pprint
import numpy
from deap import base, creator, tools, algorithms
from sudoku import Sudoku

PENALTY_DUPLICATES = 100
PENALTY_BLANKS = 1
PENALTY_NO_VALUES = 100

POPULATION_SIZE = 1000
MUTATION_RATE = 0.05

FITNESS_MODEL = Sudoku()


def evaluate(list_repr):
    """ Returns the fitness of a given puzzle. """
    FITNESS_MODEL.recreate_from_list(list_repr)
    fitness = 0
    fitness -= count_total_duplicates(FITNESS_MODEL) * PENALTY_DUPLICATES
    # fitness -= count_total_blanks(FITNESS_MODEL) * PENALTY_BLANKS
    for row in range(FITNESS_MODEL.SIZE):
        for col in range(FITNESS_MODEL.SIZE):
            if FITNESS_MODEL.get_cell(row, col) == 0:
                fitness -= PENALTY_BLANKS
                if not FITNESS_MODEL.get_possible_values(row, col):
                    fitness -= PENALTY_NO_VALUES
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


def main():
    creator.create('FitnessMax', base.Fitness, weights=(1.0,))
    creator.create('Individual', list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register('attr_val', random.randint, 0, 9)

    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_val, 81)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    toolbox.register('evaluate', evaluate)
    toolbox.register('mate', tools.cxTwoPoint)
    toolbox.register('mutate', tools.mutUniformInt, low=1, up=9, indpb=MUTATION_RATE)
    toolbox.register('select', tools.selTournament, tournsize=3)

    pop = toolbox.population(n=POPULATION_SIZE)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register('avg', numpy.mean)
    stats.register('std', numpy.std)
    stats.register('min', numpy.min)
    stats.register('max', numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                                   halloffame=hof, verbose=True)

    winner = Sudoku()
    winner.recreate_from_list(hof[0])
    pprint.pprint(winner.grid)
    return pop, log, hof


if __name__ == '__main__':
    main()
