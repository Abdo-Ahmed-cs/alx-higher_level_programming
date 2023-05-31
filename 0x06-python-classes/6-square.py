#!/usr/bin/python3
"""defining a square class based on last task"""


class Square:
    """starting class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing function

        Args:
            size (int): the size of the square
            position (int, int): set contains position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        """print # sign number size of times"""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")

    @property
    def position(self):
        """retrieve the value of the positoin
        Returns:

            (int, int): a tuple of positions
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """set a value for position

        Args:
            value (int, int): a positions tuple
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
