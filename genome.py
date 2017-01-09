#Contains the Genome for MOGA, Add genome elements here
from random import randint
from constants import MOGA_constants
from utils import generate_genome, scale_genome
from problem import problem_instance as p
class genome(object):
    def __init__(self):
        #Members are pretty self explanatory
        self.rank = None;
        self.crowding_distance = None;
        self.np = 0; #Stores Domination Count
        self.Sp = set(); #Set of all values dominated by the genome.  
        self.gene = None;
        self.fitnesses=[];
    def initialize(self):
        self.gene = generate_genome();
        #print self.gene;
        self.gene = scale_genome(self.gene);
        #print self.gene;
    def evaluate_fitness(self): 
        #if(p.fitness_1(self.gene)):
        self.fitnesses.append(p.fitness_1(self.gene));
        #if(p.fitness_2(self.gene)):
        self.fitnesses.append(p.fitness_2(self.gene))
    def increment_np(self):
        self.np+=1;
    def add_Sp(self,genome):
        self.Sp.add(genome);



