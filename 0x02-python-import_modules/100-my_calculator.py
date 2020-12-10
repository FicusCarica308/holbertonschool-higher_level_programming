#!/usr/bin/python3
#this program uses calculator_1 module to interpret input into a calculator
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    ops = "+/*-"
    av = sys.argv
    av_lgt = len(av) - 1

    if av_lgt != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(av[1])
    b = int(av[3])
    for i in ops:
        if av[2] == i:
            if i == '+':
                print("{0} + {1} = {2}".format(a, b, add(a, b)))
                exit(0)
            elif i == '-':
                print("{0} - {1} = {2}".format(a, b, sub(a, b)))
                exit(0)
            elif i == '*':
                print("{0} * {1} = {2}".format(a, b, mul(a, b)))
                exit(0)
            elif i == '/':
                print("{0} / {1} = {2}".format(a, b, div(a, b)))
                exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
