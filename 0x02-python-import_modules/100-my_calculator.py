#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg_len = len(sys.argv)

    if arg_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if (operator == "+"):
            result = add(a, b)
        elif (operator == "-"):
            result = sub(a, b)
        elif (operator == "*"):
            result = mul(a, b)
        elif (operator == "/"):
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        
        if result:
            print("{} {} {} = {}".format(a, operator, b, result))
