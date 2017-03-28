# Genome File
import moga_constant as c
from random import randint



class genome(object):
    def __init__(self):
        # Fundamentals
        self.gene = None  # The actual Value of the gene
        self.front = None  # The front in which the genome lies. front = rank
        # Stores the values of the gene along each objective function
        self.objective_function_values = []
        # Used for non dominated Sorting
        self.np = None  # Domination Count according to NSGA
        self.Sp = []  # Set of genomes dominated by the gene.
        # Used for Crowding distance
        self.crowding_distance = None

    def generate_genome(self):
        self.gene = randint(0, (2**c.LENGTH_OF_BIT_STRING) - 1)

    def print_genome(self):
        print 'Gene: ' + repr(self.gene)\
            + 'np: ' + repr(self.np)\
            + 'Crowding Distance: ' + repr(self.crowding_distance)


foo = genome()
foo.generate_genome()
foo.print_genome()
