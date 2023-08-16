#!/usr/bin/python3
# Author: Dtechguru

# a new func here (my_list) assigned to [] a list
def weight_average(my_list=[]):
    if not my_list:  # an if not statement []
        return 0  # 0 sis to be returned here

    num = 0
    den = 0
# for loop
    for tup in my_list:
        # looping through num and den(Dtechguru)
        num += tup[0] * tup[1]

        den += tup[1]

# final return statement
    return (num / den)
