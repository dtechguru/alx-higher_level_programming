#!/usr/bin/python3
# lets list how the code will run
# import function will be called first 
import random
# import will then be assigned to a variable name
number = random.randint(-10000, 10000)
# we will begin an if else statement
if number < 0:
# we will be using an operator called modulus here for findinf average
    last_num = number % -10
# elif  simply means elseif meaning  if  otherwise
elif number >= 0:
# just playing now ignore
    last_num = number % 10
if last_num > 5:
# am Dtechguru by the way
    print(f"Last digit of {number} is {last_num} and is greater than 5")
# not sure i introduced myself all this while
elif last_num == 0:
# am so happy doing this
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
# and we are done

