from genome import genome
#from utils import dominates
#Used to store a single population/generation

class population(object):
    def __init__(self):
        self.population=[]
        self.fronts=[]

    def insert(self, genome):
        self.population.append(genome)

    def print_pop(self):
        for i in iter(self.population):
            print ' gene ' + repr(i.gene) + ' np ' + repr(i.np) 

    def perform_nondominated_sorting(self):
        temp_list_for_front = []
        for i in xrange(0,len(self.population)):
            for j in xrange(0,len(self.population)):
                if(i!=j):
                    a = self.population[i]
                    b = self.population[j]
                    if(a.dominates(b)):
                        a.add_Sp(b); #Add b to dominated solutions set
                    elif (b.dominates(a)):
                        a.increment_np(); #add B's domination count. 
            if (self.population[i].np==0):
                #Domination Count is 0 so we can add it to the first front. 
                temp_list_for_front.append(self.population[i])

        #At this point domination counts of every population member should be finalized.
        self.fronts.append(temp_list_for_front) #doesn't copy I don't think. 
        # print 'FRONTS----------------'
        # print self.fronts[0]
        for i in xrange(0,len(temp_list_for_front)):
            


    #TODO: ADD ORGANIZATION OF ELEMENTS INTO FRONTS BASED UPON Np and Sp
                
parents = population() #stores a generation

for i in xrange(10):
    i = genome()
    i.initialize()
    i.evaluate_fitness()
    parents.insert(i)
print 'POPULATION \n---------------------------------------------'
parents.print_pop()
print '-------------------------------------------------------------'

parents.perform_nondominated_sorting()
parents.print_pop()
# for i in xrange(10):  
#     j= list(parents.population[i].Sp)
#     print j

# for i in iter(parents.population):
#     print 'GENE' + str(i.gene) + 'np '+ str(i.np)
    
