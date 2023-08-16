#!/usr/bin/python3
# haven't understand the work of matrix too well
def print_matrix_integer(matrix=[[]]):
    # but seems it should do what i need it to here
    for row in matrix:
        # a for stateme is  "Dtechgur"
        for col in row:
            # done creating what we want our new variable do
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
        # "Dtechguru"
