import random
import functions as f


def crossover(lovers):
    indices = list()
    sub_trees = list()
    for lover in lovers:
        inds = [i for i, x in enumerate(lover) if f.is_operator(x)]
        index = random.choice(inds)
        indices.append(index)
        sub_trees.append(f.find_subtree(lover, index))

    l1 = (lovers[0][:indices[0]] + sub_trees[1] +
          lovers[0][indices[0]+len(sub_trees[0]):])
    l2 = (lovers[1][:indices[1]] + sub_trees[0] +
          lovers[1][indices[1]+len(sub_trees[1]):])

    return [l1, l2]


def simple_mut(chrom):
    i = random.choice(range(len(chrom)))
    if f.is_operator(chrom[i]):
        new_chrom = chrom[:i] + f.r_operator() + chrom[i+1:]
    else:
        new_chrom = chrom[:i] + f.r_operand() + chrom[i+1:]


    return new_chrom


def mutation(chrom):
    inds = [i for i, x in enumerate(chrom) if f.is_operator(x)]
    index = random.choice(inds)
    sub_tree = f.find_subtree(chrom, index)
    mut_tree = f.generate(0)

    return (chrom[:index] + mut_tree +
            chrom[index+len(sub_tree):])


def gen_pop(pop_size):
    return list(map(lambda x: f.generate(0), range(pop_size)))
