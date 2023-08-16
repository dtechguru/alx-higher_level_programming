#!/usr/bin/python3
# |->5-no_c.py<-|
# this variable name sounds nice it sounds like don't copy

# a def func will be declared to create my special func
# our new function will always remove c and C in when called
def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
# There we have it all done "Dtechguru"
