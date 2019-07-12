import random
import functions as f
import genetic_functions as genetik


def gen_pop(pop_size):
    return list(map(lambda x: f.generate(0), range(pop_size)))


def gen_fit(pop, goal):
    for i in pop[:10]:
        print(i)
        print()
    evals = list(map(lambda x: f.evaluate(x), pop))
    fits = list(map(lambda x: abs(goal - x), evals))
    fit_pop = list(zip(fits, pop))
    fit_pop.sort()
    ordered_pop = list(zip(*fit_pop))[1]

    return ordered_pop, fit_pop[0][0], fit_pop[1][0]


def evolve(pop, best_Fitness, fit_2, pop_size, goal):
    n_gens = 100
    elite_perc = .1
    the_Best = pop[0]
    second = pop[1]
    print("Generation_0::")
    print("\tBest_Fitness:: {}".format(best_Fitness))

    l = int(len(pop)*elite_perc)
    for gen in range(1, n_gens + 1):
        next_gen = [the_Best, second]
        elite = pop[:l]
        while len(next_gen) < pop_size:
            next_gen.extend(genetik.crossover(random.sample(elite, 2)))

        new_o_pop, pop_best, s = gen_fit(next_gen, goal)
        
        if pop_best < best_Fitness:
            best_Fitness = pop_best
            the_Best = new_o_pop[0] 
        if s < fit_2:
            fit_2 = s
            second = new_o_pop[1]
        
        print("\tBest_Fitness:: {}".format(best_Fitness))
        print("Generation_{}".format(gen))


def main():
    pop_size = 1000
    n = random.randrange(500, 5001)
    print("The number is:: {}".format(n))

    pop = gen_pop(pop_size)
    ordered_pop, best_fit, fit_2 = gen_fit(pop, n)
    evolve(ordered_pop, best_fit, fit_2, pop_size, n)

if __name__ == '__main__':
    main()
