from random import randint
from constants import MOGA_constants
from problem import problem_instance as p
from genome import genome

def generate_genome():
    ##Generates a random bitstring
    return randint(0,(2**MOGA_constants.LENGTH_OF_BIT_STRING)-1) #generate a 32 bit bit string
    
def scale_genome(gene):
    #Takes a bound input(bounds are stored in Problem) and maps the genome to a scaled value
    return  p.lower_bound+(p.upper_bound-p.lower_bound)*gene/((2**MOGA_constants.LENGTH_OF_BIT_STRING)-1)
    
def dominates(genome_1,genome_2):
    flag = False;
    temp = []
    for i in xrange(0,p.number_of_objectives-1):
        temp.append(0)
        temp[i] = genome_1.fitnesses[i]-genome_2.fitnesses[i]#Case Completely dominates
    sum = 0.0
    for i in temp:
        sum+=i

    if(sum>0.0):
        return True 
    #should return True if Genome_1 dominates Genome_2
    else:
        return False
