#!/usr/bin/python3
# Auth: dtechguru

# define our func here
def square_matrix_map(matrix=[]):
    # return statement (y,y,2,matrix)
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
# a simple code
