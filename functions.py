import random

operators = "+-*/"
operands = "123456789"


def is_operand(val):
    return val in operands


def r_operand():
    return random.choice(operands)


def r_operator():
    return random.choice(operators)


def generate(depth, p):
    tree = ""
    if depth > 50:
        p = 1

    if random.random() < p:
        return r_operand()
    else:
        depth += 1
        tree += r_operator() + generate(depth, p) + generate(depth, p)

    return tree


def evaluate(exp):
    if exp.isdigit():
        return float(exp)
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
                # return "Cannot divide by zero"
                stack.append(0)

    return float(stack[0])


def main():
    exp = generate(0, .5)
    if len(exp) == 1:
        solution = exp
    else:
        solution = evaluate(exp)

    print("Expression::\n\t{}".format(exp))
    print("Solution::\n\t{}".format(solution))

if __name__ == '__main__':
    main()
