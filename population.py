from genome import genome
#Used to store a single population/generation

class population(object):
    def __init__(self):
        self.population=[]
        self.fronts=[]

    def insert(self, genome):
        self.population.append(genome)

    def print_pop(self):
        for i in iter(self.population):
            print i.gene


