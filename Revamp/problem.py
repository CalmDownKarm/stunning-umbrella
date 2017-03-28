# Contains all information about the problem - the fitness functions, the
# bounds to the searchspace, etc


class Problem(object):
    # def __init__(self):
    lower_bound = -1000
    upper_bound = 1000
    number_of_objectives = 2


# You want multiple objective functions for a single variable
# Eventually we need to add support to fveind the intersection of various
# search spaces
    def fitness_1(self, x):
        return x * x

    def fitness_2(self, x):
        return (x-2)**2


problem_instance = Problem()
