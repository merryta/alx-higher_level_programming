#!/usr/bin/python3
'''
Definess a square
'''


class Square():
    '''
    class represents a square

    Args:
    size(int): size of square
    '''
    def __init__(self, size=0):
        '''
        initialization of instance attributes
        Args:
        size(int): size of square
        '''
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
