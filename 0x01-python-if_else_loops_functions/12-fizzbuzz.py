#!/usr/bin/python3
# Dtechguru Dtechguru:"12-fizzbuzz.py"
# in this code you will notice all print statement does not accept newline
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
# Dtechguru this is "12-fizzbuzz.py" project
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")
# By Dtechguru

