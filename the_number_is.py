import random
import functions as f


def gen_pop(pop_size):
    return list(map(lambda x: f.generate(0, .5), range(pop_size)))


def gen_fit(pop, goal):
    evals = list(map(lambda x: f.evaluate(x), pop))
    fits = list(map(lambda x: abs(goal - x), evals))
    fit_pop = list(zip(fits, pop))
    fit_pop.sort()


def main():
    pop_size = 1000
    n = random.randrange(501)
    print("The number is:: {}".format(n))

    pop = gen_pop(pop_size)
    fit = gen_fit(pop, n)


if __name__ == '__main__':
    main()
