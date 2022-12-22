#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size #: size of the square
