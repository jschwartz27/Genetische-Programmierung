import random

operators = "+-*/"
operands = "123456789"


def is_operand(val):
    return val in operands


def r_operand():
    return random.choice(operands)


def r_operator():
    return random.choice(operators)


def generate_L():
    tree = list()
    if random.random() < .5:
        return r_operand()
    else:
        tree.extend([r_operator(), generate_L(), generate_L()])

    return tree


def evaluate_L(exp):
    for i in range(1, 3):
        if len(exp[i]) != 1:
            exp[i] = evaluate(exp[i])

    return eval("{}{}{}".format(exp[1], exp[0], exp[2]))


def generate():
    tree = ""
    if random.random() < .5:
        return r_operand()
    else:
        tree += r_operator() + generate() + generate()

    return tree


def evaluate(exp):
    exp = list(exp)
    exp.reverse()
    stack = list()
    for i in exp:
        if is_operand(i):    
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            try:
                stack.append(eval("{}{}{}".format(a, i, b)))
            except:
                return "Cannot divide by zero"
            # stack.append(val)

    return stack[0]


def main():
    exp = generate()
    if len(exp) == 1:
        solution = exp
    else:
        solution = evaluate(exp)

    print("Expression::\n\t{}".format(exp))
    print("Solution::\n\t{}".format(solution))

if __name__ == '__main__':
    main()
