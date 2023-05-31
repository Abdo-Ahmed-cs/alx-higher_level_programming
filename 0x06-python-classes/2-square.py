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

