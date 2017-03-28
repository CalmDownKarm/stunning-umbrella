# Contains all information about the problem - the fitness functions, the
# bounds to the searchspace, etc


class Problem(object):
    # def __init__(self):
    lower_bound = 0.0
    upper_bound = 2.0
    number_of_objectives = 2


# You want multiple objective functions for a single variable
# Eventually we need to add support to fveind the intersection of various
# search spaces
    def fitness_1(self, x):
        return x * x

    def fitness_2(self, x):
        return 1.0 / x


problem_instance = Problem()
