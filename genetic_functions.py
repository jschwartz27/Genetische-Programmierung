import random
from functions import find_subtree


def crossover(lovers):
    indices = list()
    for lover in lovers:
        inds = [i for i, x in enumerate(lover) if x in "+-*/"]
        indices.append(random.choice(inds))

    l1 = lovers[0][:indices[0]] + lovers[1][indices[1]:]
    l2 = lovers[1][:indices[1]] + lovers[0][indices[0]:]

    return [l1, l2]


def gen_pop(pop_size):
    return list(map(lambda x: f.generate(0), range(pop_size)))
