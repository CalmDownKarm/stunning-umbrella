# Handles all the code for each generation
import moga_constant as c
from genome import genome
import numpy.random as r

class generation(object):
    def __init__(self):
        # Stores all the members of the current generation Set
        self.population_members = []
        self.fronts = []  # Stores all the fronts for each generation.

    def initialize(self):
        for i in xrange(0, c.POPULATION_SIZE):
            i = genome()
            i.evaluate_objective_functions()
            self.population_members.append(i)

    def print_population(self):
        print '----Population Begin---------'
        for i in self.population_members:
            i.print_genome()
            print '----'
        print '----------Population End-----'

    def run_tournament(self):
    	if(self.population_members[0].crowding_distance==None):
    		# if crowding distance isn't set use only front. 
    		for i in xrange(0,len(self.population_members)):
    			




    # def binary_tournament_selection(self):
    # 	# Pick 2 random numbers in the population
    # 	# Then use the simulated binary crossover as defined
    # 	# in the docs
    # 	count = 0
    # 	for i in xrange(0,len(self.population_members)/2):
    # 		print i
    # 		p = r.randint(0,len(self.population_members),2)
    # 		if(p[0]==p[1]):
    # 			count+=1
    # 	print 'number of clashes' +repr(count/10000)
    	

foo = generation()
foo.initialize()
# foo.print_population()
#foo.binary_tournament_selection()