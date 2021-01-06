#!/usr/bin/python3
"""This is a class that mimicks a C programs singly linked list"""


class Node:
    """private field initialization"""
    def __init__(self, data, next_node=None):
        """calls getter methods data and next_node 
        to initilize private attributes
        """
        self.data = data
        self.next_node = next_node
    #----------------------__data atribute methods
    @property
    def data(self):
        """getter property for private attribute __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter to set ___data private attribute"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    #----------------------__next_node attribute methods
    @property
    def next_node(self):
        """getter property for private attribute __next_node"""
        return self.__next_node

    @data.setter
    def next_node(self, value):
        """setter to set __next_node private attribute"""
        #if type(next_node) is not Node:
         #   raise TypeError("next_node must be a Node object")
        #else:
        self.__next_node = value
    #------------------------------------------------------
"""Class called singly linkes list"""


class SinglyLinkedList:
    """    """
    def __init__(self):
        self.__head = Node(0)

    def sorted_insert(self, value):
        new_node = Node(value)
        cur = self.__head
        while cur.next_node() != None:
            cur = cur.__next_node
        cur.__next_node = new_node