#!/usr/bin/python3
"""0-rectangle module"""



class Rectangle:
    """
    class is rectangle

    Args:
    value(int): weidth of rectangle
    value(int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        ''' 
        initalize the rectangle
        Args:
        width(int): widtht of the rectangle
        height(int): height of the rectangel
        '''
        self.__width = width
        self.__height = height
    @property
    def width(self):
        '''
        privat instance attribut width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        """
        check width 
        Args:
        value: must be intger and grater than zero
        """
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    
    @property
    def height(self):
        '''
        privat instance attribute height
        '''
        return self.__height

    
    @height.setter
    def height(self, value):
        """
        Check height
        Args:
        Value: must be integer and grater zero
        """
        if type(value) is not int:
            raise TypeError("hight must be integer")
        if value < 0:
            raise ValueError("hight must be >= 0")
        self.__height = value
    
