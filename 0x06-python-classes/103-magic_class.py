#!/usr/bin/python3
import math


class MagicClass:
    """the start of the Magicclass"""

    def __init__(self, radius):
        """init function
        Args:
            radius: the radius of the shape
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
            self.__radius = None
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
