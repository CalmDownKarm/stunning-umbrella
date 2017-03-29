# Handles all the code for each generation
import moga_constant as c
from genome import genome
import numpy.random as r
import random


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
        temp_list_for_front = []
        sorted_ele = 0
        for i in self.population_members:
            for j in self.population_members:
                if(i != j):
                    if(i.dominates(j)):
                        i.Sp.add(j)
                    elif(j.dominates(i)):
                        i.np += 1
            if(i.np == 0):
                i.front = front_counter
                temp_list_for_front.append(i)
        print "sorted element pre update" + repr(sorted_ele)
        sorted_ele += len(temp_list_for_front)
        while((sorted_ele <= len(self.population_members))or
                (front_counter < len(self.population_members))):
            previous_front = temp_list_for_front
            temp_list_for_front = []
            front_counter += 1
            for x in previous_front:
                for y in x.Sp:
                    y.np -= 1
                    if(y.np == 0):
                        y.front = front_counter
                        temp_list_for_front.append(y)
            if(temp_list_for_front):
                sorted_ele += len(temp_list_for_front)
            else:
                sorted_ele = len(self.population_members) + 1
        
        self.no_of_fronts = front_counter-1
        # print 'sorted-elements' + repr(sorted_ele) + \
        #     'Len of temp front' + repr(len(temp_list_for_front))

    def calculate_crowding_distance(self):
        new_members = []
        for front_no in xrange(1, self.no_of_fronts + 1):
            temp = []
            for member in self.population_members:
                if member.front == front_no:
                    temp.append(member)
            if(len(temp)==1):
            	temp[0].crowding_distance = float('inf')
            else:
	            for member in temp:
	                member.crowding_distance = 0
	            for y in xrange(0, p.number_of_objectives):
	                temp.sort(key=lambda x: x.objective_function_values[y])
	                temp[0].crowding_distance = float("inf")
	                temp[len(temp) - 1].crowding_distance = float("inf")
	                for i in xrange(1, len(temp) - 1):
	                    temp[i].crowding_distance += (temp[i + 1].objective_function_values[y] - temp[i - 1].objective_function_values[
	                                                  y]) / (temp[len(temp) - 1].objective_function_values[y] - temp[0].objective_function_values[y])
            for boob in temp:
            	new_members.append(boob)
        self.population_members = []
        self.population_members = new_members

    # def simulated_binary_crossover(parent_1,parent_2):
	   #  u= random.uniform(0,1)
	   #  if u <= 0.5:
	   #      beta = (2*u)**(1/(n+1))
	   #  else:
	   #      beta = 1/((2*(1-u))**(1/(n+1)))

	   #  child_1 = 0.5*((1+beta)*parent_1+(1-beta)*parent_2) 
	   #  child_2 = 0.5*((1-beta)*parent_1+(1+beta)*parent_2)
	   #  return (child_1,child_2)

	# def polynomial_mutation(parent):
	#     c.MUTATION_INDEX = 20 # read from constant.py
	#     u= random.uniform(0,1)
	#     if u<0.5:
	#         variation = ((2*u)**(1.0/mutation_index+1))-1
	#     else:
	#         variation = 1-((2*(1-u))**(1.0/mutation_index+1))

	#     return parent + (p.upper_bound - p.lower_bound)*variation

foo = generation()
foo.initialize()

foo.perform_non_dominated_sort()
foo.calculate_crowding_distance()


foo.population_members.sort(key=lambda x: x.front, reverse = True)
foo.print_population()

#foo.create_mating_pool(True)
#print 'MATING POOL'
#for x in foo.matingpool:
#    x.print_genome()
