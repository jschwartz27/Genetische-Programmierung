import random
import functions as f
import genetic_functions as genetik


def gen_fit(pop, goal):
    evals = list(map(lambda x: f.evaluate(x), pop))
    fits = list(map(lambda x: abs(goal - x), evals))
    fit_pop = list(zip(fits, pop))
    fit_pop.sort()
    ordered_pop = list(zip(*fit_pop))[1]

    return ordered_pop, fit_pop[0][0], fit_pop[1][0]


def evolve(pop, best_Fitness, fit_2, pop_size, n_gens, mut_rate,
           elite_perc, goal):
    the_Best = pop[0]
    second = pop[1]
    print("Generation_0::")
    print("\tBest_Fitness:: {}".format(best_Fitness))

    l = int(len(pop)*elite_perc)
    for gen in range(1, n_gens + 1):
        next_gen = [the_Best, second]
        elite = pop[:l]
        while len(next_gen) < pop_size:
            crossed_lovers = genetik.crossover(random.sample(elite, 2))
            for i in range(len(crossed_lovers)):
                if random.random() < mut_rate:
                    crossed_lovers[i] = genetik.mutation(crossed_lovers[i])
            next_gen.extend(crossed_lovers)

        new_o_pop, pop_best, s = gen_fit(next_gen, goal)

        if pop_best < best_Fitness:
            best_Fitness = pop_best
            the_Best = new_o_pop[0]
        if s < fit_2:
            fit_2 = s
            second = new_o_pop[1]

        print("\nGeneration_{}".format(gen))
        print("\tBest_Fitness:: {}".format(best_Fitness))
        print("\t{}".format(the_Best))

        if best_Fitness == 0:
            break

    return (best_Fitness, the_Best)


def main():
    pop_size = 1000
    n_gens = 2000
    mut_rate = .05
    elite_perc = .1
    n = random.randrange(500, 5001)
    print("The number is:: {}".format(n))

    pop = genetik.gen_pop(pop_size)
    ordered_pop, best_fit, fit_2 = gen_fit(pop, n)
    der_Übermensch = evolve(
        ordered_pop, best_fit, fit_2, pop_size,
        n_gens, mut_rate, elite_perc, n
    )

    if der_Übermensch[0] == 0:
        print("\n{} == {}".format(der_Übermensch[1], n))
    else:
        print("\n{}".format(der_Übermensch[1]))
        print("\tFinal_fitness:: {}".format(der_Übermensch[0]))

if __name__ == '__main__':
    main()
