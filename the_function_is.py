import random
import functions as f
import genetic_functions as genetik

functions = {
    "1": [
        "**xxx",      # x**3
        "***xxxx",    # x**4
        "+*xxx",      # x**2 + x
        "+*xx*4x"     # x**2 + 4x
        ],
    "2": [
        "**xxy",      # x**2 * y
        "+**xxx*yy",  # x**3 + y**2
        "+*2*xx*3y"   # 2x**2 + 3y
    ],
    "3": [
        "*2+*xy*zz",  # 2(xy + z**2)
        "**xyz",      # xyz
        "++*xx*yyz"   # x**2 + y**2 + z
    ]
}


def create_samples(func, n_vs):
    sample_n = 3
    ns = "xyz"
    sample_dict = dict()
    for i in range(sample_n):
        vs = {j: random.choice(range(1,21)) for j in ns[:n_vs]}
        e = f.evaluate_Vs(func, vs)
        sample_dict[str(vs)] = e
    
    return sample_dict


def evolve_Vs(samples, pop_size, n_gens, mut_rate, elite_perc):
    pass


def main():
    pop_size = 1000
    n_gens = 2000
    mut_rate = .1
    elite_perc = .1
    n_vs = random.choice(range(1,4))
    function = random.choice(functions[str(n_vs)])
    sample_dict = create_samples(function, n_vs)

    result = evolve_Vs(sample_dict, pop_size, n_gens, mut_rate, elite_perc)

    print("The function is:: {}".format(function))
    print("Trained with the following data points::")
    print("\t{}".format(sample_dict))

if __name__ == '__main__':
    main()
