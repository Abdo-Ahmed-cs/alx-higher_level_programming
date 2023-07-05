#!/usr/bin/python3
"""
defining the rectangle class
"""


class Rectangle:
    """
    rectangle class defines a rectangle shape with i
    attributes
    """
    def __init__(self, width=0, height=0):
        """
        NOTE:
            initializing method for rectangle object
        ARGS:
            width: rectangle width
            height: rectangle height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        this method is used as a getter for width attr
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this methos is used as a setter for width attr
        ARGS:
            value: the value for the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        this method is used as a getter for height attr
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        this methos is used as a setter for height attr
        ARGS:
            value: the value for the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        a function that returns the area of the rect
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        a function that returns the perimeter of the rect
        """
        return (self.__width + self.__height) * 2
