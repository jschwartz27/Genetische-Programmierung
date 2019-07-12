import random
from operator import add, sub, mul

operators = "+-*/"
operands = "123456789"


def exp(a, b):
    return a**b


def div(a, b):
    if b == 0:
        return 0
    else:
        return a / b

ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "$": exp
}


def r_operand():
    return random.choice(operands)


def r_operator():
    return random.choice(operators)


def generate(depth):
    tree = ""
    if depth > 3:
        return r_operand()

    if random.random() < .5:
        return r_operand()
    else:
        depth += 1
        tree += r_operator() + generate(depth) + generate(depth)

    return tree


def evaluate(exp):
    if exp.isdigit():
        return float(exp)
    exp = list(exp)
    exp.reverse()
    stack = list()
    for val in exp:
        if val in operands:
            stack.append(val)
        else:
            a = float(stack.pop())
            b = float(stack.pop())
            try:
                stack.append(ops[val](a, b))
            except:
                # TODO this must be fixed
                # print(a, b, val)
                return 10101010101

    return float(stack[0])


def find_subtree(exp, index):
    pass


def main():
    exp = generate(0)
    if len(exp) == 1:
        solution = exp
    else:
        solution = evaluate(exp)

    print("Expression::\n\t{}".format(exp))
    print("Solution::\n\t{}".format(solution))

if __name__ == '__main__':
    main()
