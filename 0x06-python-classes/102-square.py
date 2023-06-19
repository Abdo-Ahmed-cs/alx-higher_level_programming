#!/usr/bin/python3
"""defining a square class based on last task"""


class Square:
    """starting class Square"""

    def __init__(self, size=0):
        """initializing function

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area function

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ a getter function for the size

        Returns:
            int: size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ a setter function for the square size

        Args:
            value (int): the value specified for the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __repr__(self):
        return str(self.area())

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size
