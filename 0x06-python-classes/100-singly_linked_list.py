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
# ----------------------__data atribute methods
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
# ----------------------__next_node attribute methods
    @property
    def next_node(self):
        """getter property for private attribute __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter to set __next_node private attribute"""
        # if type(next_node) is not Node:
         #   raise TypeError("next_node must be a Node object")
        # else:
        self.__next_node = value
    # ------------------------------------------------------
"""Class called singly linkes list"""


class SinglyLinkedList:
    """class that intializes a sorted linked list (least to greatest"""
    def __init__(self):
        """Creates head node object in private field"""
        self.__head = None

    def sorted_insert(self, value):
        """When called this method will add a new node to the list
        while at the same time sorting them into the correct position
        """
        new_n = Node(value)
        temp = self.__head
        if temp is None:
            self.__head = new_n
            return
        if temp.data > value:
            new_n.next_node = temp
            self.__head = new_n
            return
        while temp.next_node:
            if int(temp.next_node.data) > value:
                break
            temp = temp.next_node
        new_n.next_node = temp.next_node
        temp.next_node = new_n

    def __str__(self):
        """When print is called on our class this will print them out
        with a number on each line for the length of the linked list
        """
        output = ""
        ptr = self.__head 
        while ptr:
            if ptr.next_node is not None:
                output += str(ptr.data) + "\n"
            else:
                output += str(ptr.data)
            ptr = ptr.next_node
        return output
