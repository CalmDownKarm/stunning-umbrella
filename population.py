from genome import genome
from utils import dominates
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
    
    def perform_nondominated_sorting(self):
        for i in xrange(0,len(self.population)):
            for j in xrange(0,len(self.population)):
                if(i!=j):
                    a = self.population[i]
                    b = self.population[j]
                    if(dominates(a,b)):
                        a.add_Sp(b);
                        b.increment_np();
                    elif (dominates(b,a)):
                        b.add_Sp(a);
                        a.increment_np();
                
parents = population() #stores a generation
for i in xrange(10):
    i = genome()
    i.initialize()
    i.evaluate_fitness()
    parents.insert(i)

parents.perform_nondominated_sorting()
for i in xrange(10):  
    i= list(parents.population[i].Sp)
    print i[0].gene;
    
