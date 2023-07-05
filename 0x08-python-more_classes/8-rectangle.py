#!/usr/bin/python3
"""
defining the rectangle class
"""


class Rectangle:
    """
    rectangle class defines a rectangle shape with i
    attributes
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """
        prints the reactangle in a nicely printable string format
        the reactangle instance will be printed filled width '#' char
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ''
        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.__width
            rect_str += '\n'
        return rect_str[0:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
