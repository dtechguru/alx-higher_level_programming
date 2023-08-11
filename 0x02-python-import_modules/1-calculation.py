#!/usr/bin/python3
# an if statement will be mentiond here
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div  # dtechguru

# here i will assign two numbers to a, b
    a = 10
    b = 5

# "Dtechguru" the code is looking dope
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
