# Handles all the code for each generation
import moga_constant as c
from genome import genome
import numpy.random as r


class generation(object):
    def __init__(self):
        # Stores all the members of the current generation Set
        self.population_members = []
        self.fronts = []  # Stores all the fronts for each generation.
        self.matingpool = []  # Stores Mating Pool for the current Crossover
        self.no_of_fronts = None  # Stores total Number of fronts.

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

    def create_mating_pool(self, flag):
        # call flag as true if first iteration. else false
        # Run the tournament and return a matingpool
        if(flag):
            # if crowding distance isn't set use only front.
            while(len(self.matingpool) < len(self.population_members)):
                p = r.randint(0, len(self.population_members), 2)
                if(p[0] != p[1]):
                    geneA = self.population_members[p[0]]
                    geneB = self.population_members[p[1]]
                    if geneA.front < geneB.front:
                        self.matingpool.append(geneA)
                    elif geneA.front > geneB.front:
                        self.matingpool.append(geneB)
                    else:
                        self.matingpool.append(geneA)
                        self.matingpool.append(geneB)
        else:
            while(len(self.matingpool) < len(self.population_members)):
                p = r.randint(0, len(self.population_members), 2)
                if(p[0] != p[1]):
                    geneA = self.population_members[p[0]]
                    geneB = self.population_members[p[1]]
                    if geneA.front < geneB.front:
                        self.matingpool.append(geneA)
                    elif geneA.front > geneB.front:
                        self.matingpool.append(geneB)
                    else:
                        if geneA.crowding_distance > geneB.crowding_distance:
                            self.matingpool.append(geneA)
                        elif geneA.crowding_distance < geneB.crowding_distance:
                            self.matingpool.append(geneB)
                        else:
                            self.matingpool.append(geneA)
                            self.matingpool.append(geneB)

    def perform_non_dominated_sort(self):
    	front_counter = 1
    	for i in xrange(0,len(self.population_members)):
    		for j in xrange(0,len(self.population_members)):
    			if(i!=j):
    				a = self.population_members[i]    				
    				b = self.population_members[j]

    				if(a.dominates(b)):
    					a.Sp.add(b)
    					print 'boobs'
    				elif(b.dominates(a)):
    				#else:
    					print 'fuck'
    					a.np +=1
    				
    				
    	self.print_population()
        # temp_list_for_front = []
        # front_counter = 1
        # organized_elements = 0
        # for i in xrange(0, len(self.population_members)):
        #     for j in xrange(0, len(self.population_members)):
        #         if(i != j):
        #             a = self.population_members[i]
        #             b = self.population_members[j]
        #             if(a.dominates(b)):
        #                 a.Sp.append(b)
        #             elif(b.dominates(a)):
        #                 a.np += 1
        #     if(self.population_members[i].np == 0):
        #         self.population_members[i].front = front_counter
        #         temp_list_for_front.append(self.population_members[i])
        # self.fronts.append(temp_list_for_front)
        # organized_elements += len(temp_list_for_front)
        # while((organized_elements <= len(self.population_members))or(front_counter <= len(self.population_members) - 1)):
        # 	print "boobs"
        # 	temp = self.fronts[-1]
        # 	temp_list_for_front = []
        # 	for x in temp:
        # 		for y in x.Sp:
        # 			y.np -= 1
        #             if(y.np == 0):
        #                 y.front = front_counter
        #                 temp_list_for_front.append(y)
        #     if(temp_list_for_front):
        #         organized_elements += len(temp_list_for_front)
        #         self.fronts.append(temp_list_for_front)
        #         front_counter += 1
        #     else:
        #         organized_elements = len(self.population_members) + 1


foo = generation()
foo.initialize()
# foo.print_population()
foo.perform_non_dominated_sort()
#foo.print_population()
