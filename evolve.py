#evolve.py used to run the main loop
from population import population
from constants import MOGA_constants
from genome import genome


parents = population() #stores a generation
for i in range(MOGA_constants.POPULATION_SIZE):
    i = genome()
    i.initialize()
    i.evaluate_fitness()
    parents.insert(i)

parents.print_pop();

