from genome import genome
from random import randint
# Used to store a single population/generation


class generation(object):
    def __init__(self):
        self.population = []
        self.fronts = []
        self.matingpool = []

    def insert(self, genome):
        self.population.append(genome)

    def print_pop(self):
        for i in iter(self.population):
            i.printgenome()

    def perform_nondominated_sorting(self):
        # Takes a combined population and organizes it into fronts.
        # TODO ADD A combined population after rest of genetic operators are
        # written
        frontcounter = 1
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
                self.population[i].set_front(frontcounter)
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
        # loopcounter = 0
        while((organizedelements <= len(self.population))or
              (frontcounter <= len(self.population) - 1)):
            # while (loopcounter<10):
            # temp = copy.deepcopy(self.fronts[-1])  # copy the last front
            temp = self.fronts[-1]
            # print 'Front here----------------------'
            # for foo in temp:
            #     foo.printgenome()
            # print '------------------'
            # print 'SP of Front ------------------'
            temp_list_for_front = []
            for x in temp:
                for y in x.Sp:
                    # y.printgenome()
                    y.np -= 1
                    if(y.np == 0):
                        y.set_front(frontcounter)
                        temp_list_for_front.append(y)
            if(temp_list_for_front):
                organizedelements += len(temp_list_for_front)
                self.fronts.append(temp_list_for_front)
                frontcounter += 1
            else:
                organizedelements = len(self.population) + 1
        # self.fronts contains all the fronts at this point.
        # TODO take in an additional N population members and apply to the
        # entire combined population

    def run_tournament(self, genome1, genome2):

        if((len(self.matingpool) < len(self.population))and
           (genome1 != genome2)):
            if(genome1.front < genome2.front):
                self.matingpool.append(genome1)
            elif(genome1.front > genome2.front):
                self.matingpool.append(genome2)
            else:
                self.matingpool.append(genome1)
                self.matingpool.append(genome2)

    def run_tournament_with_crowding_distance(self, genome1, genome2):
        # win the tournament if -
        # better front (lower is better)
        # higher crowding distance.
        if((len(self.matingpool) < len(self.population))and
           (genome1 != genome2)):
            if(genome1.front < genome2.front):
                if(genome1.crowding_distance > genome2.crowding_distance):
                    self.matingpool.append(genome1)
                else
                    


    def calculate_crowding_distance(self):
        for x in self.fronts:
            if(len(x) > 1):
                # Sort based on objectives.
                sorted(x, key=lambda genome: genome.fitnesses[0])

    def tournament_selection(self):
        while(len(self.matingpool) < len(self.population)):
            # Performs the crowded tournament selection operator
            for x in self.population:
                y = self.population[randint(0, len(self.population) - 1)]
                self.run_tournament(x, y)
        # TODO: Inculcate crowded distance operator.

    def crowded_tournament_selection(self):
        # Calculate a crowding distance and rank
        return False


parents = generation()  # stores a generation

for i in xrange(10):
    i = genome()
    i.initialize()
    i.evaluate_fitness()
    parents.insert(i)
print 'POPULATION \n---------------------------------------------'
parents.print_pop()
print '-------------------------------------------------------------'
parents.perform_nondominated_sorting()
parents.tournament_selection()
parents.print_pop()
print '---------------MATINGPOOL-----------------------------'
for x in parents.matingpool:
    x.printgenome()
for x in parents.fronts:
    print '--------------------------------- CHECK----------------------'
    for y in x:
        y.printgenome()
    tempfoo = sorted(x, key=lambda genome: genome.fitnesses[0], reverse=True)
    for bob in tempfoo:
        bob.printgenome()
for x in parents.fronts:
    print '--------------------------------- CHECK POST SORT----------------------'
    for y in x:
        y.printgenome()
