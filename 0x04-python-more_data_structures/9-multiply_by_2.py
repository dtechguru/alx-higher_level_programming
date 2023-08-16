#!/usr/bin/python3
# Auth: Dtechguru

# we will define our own dynamic func [(a_dictiona)]
def multiply_by_2(a_dictionary):

    """Lets declare a variable name """
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())
# let's call a for loop here ([Dtechguru])
    for i in list_keys:
        new_dir[i] *= 2
# now our oc code should rewturn func()new_dir}
    return (new_dir)
