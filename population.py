from genome import genome;
#Used to store a single population/generation

class population(object):
	define __init__(self):
		self.population=[];
		self.fronts=[];

	define insert(self, genome):
		self.population.append(genome);

