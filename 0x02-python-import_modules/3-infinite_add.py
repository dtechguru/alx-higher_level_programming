#!/usr/bin/python3
# a calculation program

if __name__ == "__main__":
    """Print the addition of all arguments."""
# Import still havent know what it does
    import sys
# sa ve total
    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
# call the last print statement "Dtechguru"
    print("{}".format(total))
