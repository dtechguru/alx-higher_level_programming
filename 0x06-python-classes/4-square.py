#!/usr/bin/python3
# Author: Dtechguru
# A CLASS square will definately be defined here  


class Square:
    # a square is then represented here
	# now we'll create our own func
    def __init__(self, size=0):
        """Initialization of a new square will be done here .

        Args:
            size (int): te wey of te new square asin size
	Author: Dtechguru
        """
        self.size = size

    @property
    def size(self):
        """dhe current size of the square is gotten from here."""
        return (self.__size)

    @size.setter
	#ere we'll define a new func for our pro
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Author: Dtechguru"""
        return (self.__size * self.__size)
"""Author: Dtechguru"""
