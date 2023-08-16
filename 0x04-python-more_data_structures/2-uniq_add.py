#!/usr/bin/python3
# define a func that sets (my_list) returning an int
def uniq_add(my_list=[]):
    # uniq_list is set now
    uniq_list = set(my_list)
    # we will assign int O to num here
    num = 0

# now a for loop
    for i in uniq_list:
        num += i
# should return NULL
    return (num)
# Auth: Dtechguru
