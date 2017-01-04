#Contains the Genome for MOGA, Add genome elements here

class genome(object):
	def __init__(self):
		#Members are pretty self explanatory
		self.rank = None;
		self.crowding_distance = None;
		self.dominated = set();
		self.dominates = set();
		self.