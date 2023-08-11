#!/usr/bin/python3
# task 6-print_comb3.py "let's go"
# beginng with for loop
for i in range(9):
    for j in range(i + 1, 10):
# Dtechguru
# an if statement is here also
        if i * 10 + j < 89:
            print("{:d}{:d}".format(i, j), end=", ")
# Dtechguru
print("{:d}".format(89))

