#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1

    tupc = (('+', calculator_1.add), ('-', calculator_1.sub),
            ('*', calculator_1.mul), ('/', calculator_1.div))
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        for x in tupc:
            if op in x:
                c = x[1](a, b)
                print("{} {} {} = {}".format(a, op, b, c))
                break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
