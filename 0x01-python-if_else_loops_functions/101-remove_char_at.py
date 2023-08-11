#!/usr/bin/python3
# Dtechguru
# Python project : "101-remove_char_at.py"
# lets go on
def remove_char_at(str, n):
    if n < 0:
# its me Dtechguru
        return str
    else:
# Dtechguru
        str = str[0:n] + str[n+1:]
    return str

