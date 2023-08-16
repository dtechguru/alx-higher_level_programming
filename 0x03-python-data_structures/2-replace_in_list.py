#!/usr/bin/python3
# 2-replace_in_list.py
# Am Dtechguru

# i said about def in the previous code
def replace_in_list(my_list, idx, element):
    # Element of any list positio is to be replaced
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        # return statement is called now
    return (my_list)
# Dtechguru codes
