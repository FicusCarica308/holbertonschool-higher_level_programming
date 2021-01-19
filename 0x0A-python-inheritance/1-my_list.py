#!/usr/bin/python3
"""module that contains a single class Mylist()"""


class MyList(list):
    """
    Class that creates a different list object using the inherited list object
    """
    def print_sorted(self):
        """prints a sorted list instead of a normal list"""
        copy_list = list(self)
        copy_list.sort()
        print(copy_list)
