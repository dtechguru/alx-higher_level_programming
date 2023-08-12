#!/usr/bin/python3
# in this program we will be assing a varible int

# an If statement #Dtechguru#
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    # Dtechguru
    from calculator_1 import add, sub, mul, div
    import sys

# program should run fine
    if len(sys.argv) - 1 != 3:
        # this print statement will be quite tasky
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

# Here we will be calling int for the first time
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    # our final print statement "Dtechguru"
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
