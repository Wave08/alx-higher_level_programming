#!/usr/bin/python3
"""
more class base
"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
     """ definition of a Rectangle """
     def __int__(self, width, height):
         """construction and width, height"""
         self.__width = width
         self.__height = height
         BaseGeometry.integer_validator(self, "
