import random
from functions import find_subtree, generate


def crossover(lovers):
    indices = list()
    sub_trees = list()
    for lover in lovers:
        inds = [i for i, x in enumerate(lover) if x in "+-*/"]
        index = random.choice(inds)
        indices.append(index)
        sub_trees.append(find_subtree(lover, index))

    l1 = (lovers[0][:indices[0]] + sub_trees[1] +
          lovers[0][indices[0]+len(sub_trees[0]):])
    l2 = (lovers[1][:indices[1]] + sub_trees[0] +
          lovers[1][indices[1]+len(sub_trees[1]):])

    return [l1, l2]


def mutation(chrom):
    pass


def gen_pop(pop_size):
    return list(map(lambda x: generate(0), range(pop_size)))
