#!/usr/bin/python3
# def "Dtechguru"
def print_last_digit(number):
# an if statement
    if number < 0:
        last_num = (-number % 10)
# elif meaning else if 
    elif number >= 0:
        last_num = number % 10
# a prit stament to pring the above without a new line
    print("{:d}".format(last_num), end="")
    return last_num
# Dtechguru

