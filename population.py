from genome import genome
import copy
# from utils import dominates
# Used to store a single population/generation


class population(object):
    def __init__(self):
        self.population = []
        self.fronts = []

    def insert(self, genome):
        self.population.append(genome)

    def print_pop(self):
        for i in iter(self.population):
            print ' gene ' + repr(i.gene) + ' np ' + repr(i.np)

    def perform_nondominated_sorting(self):
        # Stores how many elements in the population have been organized into
        # fronts.
        organizedelements = 0
        temp_list_for_front = []
        for i in xrange(0, len(self.population)):
            for j in xrange(0, len(self.population)):
                if(i != j):
                    a = self.population[i]
                    b = self.population[j]
                    if(a.dominates(b)):
                        a.add_Sp(b)  # Add b to dominated solutions set
                    elif (b.dominates(a)):
                        a.increment_np()  # add B's domination count.
            if (self.population[i].np == 0):
                # Domination Count is 0 so we can add it to the first front.
                temp_list_for_front.append(self.population[i])

        # At this point domination counts of every population member should be
        # finalized.
        self.fronts.append(temp_list_for_front)
        # Increment the organized elements counter by the number of the
        # elements
        organizedelements += len(temp_list_for_front)
        # first front is now on the stack.
        # now pop the front at the top of the stack, look at Sp of every
        # element and decrease np by 1
        while(organizedelements <= len(self.population)):
            temp = copy.deepcopy(self.fronts[-1])  # copy the last front
            # empty the list by creating a new list and assigning the same
            # pointer
            temp_list_for_front = []
            for x in xrange(0, len(temp)):
                for y in temp[x].Sp:
                    y.np -= 1
                    if(y.np == 0):
                        temp_list_for_front.append(y)
                    


# parents = population()  # stores a generation

# for i in xrange(10):
#     i = genome()
#     i.initialize()
#     i.evaluate_fitness()
#     parents.insert(i)
# print 'POPULATION \n---------------------------------------------'
# parents.print_pop()
# print '-------------------------------------------------------------'

# parents.perform_nondominated_sorting()
# parents.print_pop()
# # for i in xrange(10):
# #     j= list(parents.population[i].Sp)
# #     print j

# # for i in iter(parents.population):
# #     print 'GENE' + str(i.gene) + 'np '+ str(i.np)
