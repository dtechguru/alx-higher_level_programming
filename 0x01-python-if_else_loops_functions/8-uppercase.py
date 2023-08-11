#!/usr/bin/python3
# lets begin Python Dtechguru

def uppercase(str):
# a for loop
    for i in str:
# an if statement Dtechguru
        if ord("a") <= ord(i) <= ord("z"):
            i = chr(ord(i) - 32)
# quite stressed
        print("{:s}".format(i), end="")
    print()

