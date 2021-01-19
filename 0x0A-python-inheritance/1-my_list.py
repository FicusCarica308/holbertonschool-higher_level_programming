#!/usr/bin/python3
"""module that contains a single class Mylist()"""


class MyList(list):
    """
    Class that creates a different list object using the inherited list object
    """
    def __init__(self):
        """will init our class with our superclass intit function"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list instead of a normal list"""
        copy_list = list(self)
        list.sort(copy_list)
        print(copy_list)
