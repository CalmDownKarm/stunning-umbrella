from random import randint
from constants import MOGA_constants
from problem import problem_instance as p
# from genome import genome


def generate_genome():
    # Generates a random bitstring
    # generate a 32 bit bit string
    return randint(0, (2**MOGA_constants.LENGTH_OF_BIT_STRING) - 1)


def scale_genome(gene):
    # Takes a bound input(bounds are stored in Problem) and maps the genome to
    # a scaled value
    return p.lower_bound + (p.upper_bound - p.lower_bound) * gene / ((2**MOGA_constants.LENGTH_OF_BIT_STRING) - 1)
