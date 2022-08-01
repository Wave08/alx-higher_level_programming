#!/usr/bin/python3
'''A module for working with geometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a geometry object
    '''
    def __init__(self, width, height):
        '''initializes a new rectangle geometry
        object with the given width and height

        Args:
        width (int): The width of a rectangle
        height (int): The height of a rectangle
        '''
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
