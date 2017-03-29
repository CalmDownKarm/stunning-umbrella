# Genome File
import moga_constant as c
from problem import problem_instance as p
from random import random


class genome(object):
    def __init__(self):
        # Fundamentals
        # The actual Value of the gene
        self.gene = random()*(2**(c.LENGTH_OF_BIT_STRING)-1)
        # Now we have to scale the genome
        self.gene = p.lower_bound + (p.upper_bound - p.lower_bound) * \
            self.gene / ((2**c.LENGTH_OF_BIT_STRING) - 1)
        self.front = None  # The front in which the genome lies. front = rank
        # Stores the values of the gene along each objective function
        self.objective_function_values = []
        # Used for non dominated Sorting
        self.np = 0  # Domination Count according to NSGA
        self.Sp = set()  # Set of genomes dominated by the gene.
        # Used for Crowding distance
        self.crowding_distance = None

    def print_genome(self):
        print 'Gene: ' + repr(self.gene)\
            + '\nfitness_1: ' + repr(self.objective_function_values[0])\
            + '\nfitness_2: ' + repr(self.objective_function_values[1])\
            + '\nnp: ' + repr(self.np)\
            + '\nFront: ' + repr(self.front)\
            + '\nCrowding Distance: ' + repr(self.crowding_distance)

    def evaluate_objective_functions(self):
        self.objective_function_values.append(p.fitness_1(self.gene))
        self.objective_function_values.append(p.fitness_2(self.gene))

    def dominates(self,genome_2):
    	greaterorequal = 0
    	for x in xrange(0,p.number_of_objectives):
    		if self.objective_function_values[x] >= genome_2.objective_function_values[x]:
    			greaterorequal+=1
    	if(greaterorequal==p.number_of_objectives):
    		return True
    	else:
    		return False

# foo = genome()
# foo.evaluate_objective_functions()
# foo.print_genome()
