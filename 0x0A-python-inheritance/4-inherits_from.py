#!/usr/bin/python3
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''the object is an inheritance of a class that inherited
    (directly or indirectly)
    obj: an object
    returns None
    '''
    return type(obj) !+ a_class and isinstance(obj, a_class)
