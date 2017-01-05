#Contains the Genome for MOGA, Add genome elements here
from random import randint
from constants import MOGA_constants
from utils import generate_genome,scale_genome
from problem import problem_instance as p
class genome(object):
	def __init__(self):
		#Members are pretty self explanatory
		self.rank = None;
		self.crowding_distance = None;
		self.dominated = set();
		self.dominates = set();
		self.gene = None;
		self.fitnesses=[];

	def initialize(self):
		self.gene = generate_genome();
		#print self.gene;
		self.gene = scale_genome(self.gene);
		#print self.gene;

	def evaluate_fitness(self):	
		if(p.fitness_1(self.gene)):
			self.fitnesses.append(p.fitness_1(self.gene));
		if(p.fitness_2(self.gene)):
			self.fitnesses.append(p.fitness_2(self.gene));
		print self.fitnesses;



