#!/usr/bin/python3
# dtechguru on the code

# time to create our special func
def square_matrix_simple(matrix=[]):
    # make use of the new func
    new_matrix = matrix.copy()
# a for loop here "Dtechguru"
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

# now a return statement
    return (new_matrix)

# 0-square_matrix_simple.py
