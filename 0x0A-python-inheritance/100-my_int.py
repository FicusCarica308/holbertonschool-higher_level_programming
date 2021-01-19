#!/usr/bin/python3
"""a module with some sketchy code"""


class MyInt(int):
    """
    A wierd code that decided it wanted to be different an swapped
    equals and not equals
    """
    def __eq__(self, other):
        """swapped from =="""
        return int(self) != int(other)

    def __ne__(self, other):
        """Swapped from !="""
        return int(self) == int(other)
