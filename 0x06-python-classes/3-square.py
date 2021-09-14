#!/usr/bin/python3
'''
Defines square by area
'''


class Square():
    '''
    reperesents a Square
    '''
    def __init__(self, size=0):
        '''
        initialization of instance atributtes
        Args:
        size(int): size of square,must be integer and greater than zero
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be grater than zero")
        self.__size = size
    def area(self):
        return self.__size ** 2
        
