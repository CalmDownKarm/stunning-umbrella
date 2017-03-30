import moga_constant as c
from generation import generation
from genome import genome
import matplotlib.pyplot as plt

p_0 = generation()
p_0.initialize()
# print 'PRE FIRST SORT'
# p_0.nigger()
p_0.perform_non_dominated_sort()
#p_0.population_members[0].print_genome()
q_0 = p_0.let_them_have_sex()
combinePandQ = generation()
combinePandQ.merge(p_0.population_members)
combinePandQ.merge(q_0)
combinePandQ.perform_non_dominated_sort()
# print 'P AND Q MERGED AND SORTED'
# combinePandQ.print_population()
p_next = combinePandQ.population_members[:c.POPULATION_SIZE]
p_t = generation()
p_t.merge(p_next)
p_t.perform_non_dominated_sort()
p_t.count_number_of_fronts()
# print 'P1 SELECTED AND SORTED'
# p_t.print_population()
iteration_counter = 0
best_fit = []
while(iteration_counter<c.NUMBER_OF_ITERATIONS):
    best_fit.append(p_t.population_members[0].gene)
    print iteration_counter
    iteration_counter+=1
    # print "------------------iteration counter : " + repr(iteration_counter)
    # p_t.print_population()
    # p_t.print_population()
    p_t.calculate_crowding_distance()
    #print iteration_counter
    p_t.create_mating_pool(False)
    q_next = p_t.let_them_have_sex()
    combinePandQ = generation()
    combinePandQ.merge(p_t.population_members)
    combinePandQ.merge(q_next)
    combinePandQ.perform_non_dominated_sort()
    p_next = combinePandQ.population_members[:c.POPULATION_SIZE]
    p_t = generation()
    p_t.merge(p_next)
    p_t.perform_non_dominated_sort()
    p_t.count_number_of_fronts()
y=[]
for x in xrange(0,c.NUMBER_OF_ITERATIONS):
    y.append(x)

print best_fit
plt.scatter(y, best_fit)
plt.show()

# foo = generation()
# bitch1 = generation()
# foo.initialize()
# foo.perform_non_dominated_sort()
# for x in xrange(0,10):
#     bitch1 = generation()
#     bitch1.initialize()
#     foo.merge(bitch1.population_members)
#     foo.perform_non_dominated_sort()
#     foo.print_population()