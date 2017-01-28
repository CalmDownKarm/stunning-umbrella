# Contains the Genome for MOGA, Add genome elements here
from random import randint
from constants import MOGA_constants
from utils import generate_genome, scale_genome
from problem import problem_instance as p


class genome(object):

    def __init__(self):
        # Members are pretty self explanatory
        self.rank = None
        self.crowding_distance = None
        self.np = 0  # Stores Domination Count
        self.Sp = set()  # Set of all values dominated by the genome.
        self.gene = None
        self.fitnesses = []
        self.fitness = 0

    def initialize(self):
        self.gene = generate_genome()
        # print self.gene;
        self.gene = scale_genome(self.gene)
        # print self.gene;

    def evaluate_fitness(self):
        # if(p.fitness_1(self.gene)):
        self.fitnesses.append(p.fitness_1(self.gene))
        # if(p.fitness_2(self.gene)):
        self.fitnesses.append(p.fitness_2(self.gene))

    def increment_np(self):
        self.np += 1

    def set_fitness(self, frontcounter):
        self.fitness = frontcounter

    def add_Sp(self, genome):
        self.Sp.add(genome)

    def printgenome(self):
        print 'Gene ' + repr(self.gene) + ' np ' +repr(self.np) + ' fitness ' + repr(self.fitness)

    def binary_crossover(self):
        # Performs a 1 point crossover
        return False

    def mutation(self):
        # Performs mutation
        return False

    # I don't think my implementation works when Im minizing cuz it assumes
    # higher fitness is better.
    def dominates(self, genome_2):
        # THIS DOMINATION FUNCTION IS JUST FUCKING WRONG. FIX THIS SHIT ASAP
        genome_1 = self
        temp = []
        for i in xrange(0, p.number_of_objectives - 1):
            temp.append(0.0)
            temp[i] = genome_1.fitnesses[i] - \
                genome_2.fitnesses[i]  # Case Completely dominates
        sum = 0.0
        for i in xrange(0, len(temp)):
            sum += temp[i]
        if(sum > 0.0):
            return True
        # should return True if Genome_1 dominates Genome_2
        else:
            return False
