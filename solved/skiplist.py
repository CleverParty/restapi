from __future__ import absolute_import, print_function

import os
import sys
import math
from random import gauss

class Node(object):
    name  = ""
    def __init__(self, level , store):
        self.name = 'Node'
        self.store = store
        # self.next_level = None
        self.level = level
        self.nextval = None

    def printValue(self):
        print("the value in this particular node is : ",self.store)

class skiplist(object):
    name = ""
    def __init__(self,value,max):
        self.name = 'skiplist'
        self.max = max
        self.value = value
        self.level = 0
        self.next = None
        self.head = self.create(self.level,-1)
        self.head.nextval = None

    def printvalue(self):
        print("the value in this node is : ",self.head.store)

    def create(self, level , key):
        obj = Node(level,key)
        return obj

    def randomize(self):
        value = gauss(int(self.level) - 1, int(self.max) - 1)

    def insertNode(self,value):
        curr_node = self.create(self.level,value)
        curr_node.store = value
        curr_node.nextval = None
        curr_node.level = 1
        if(self.head.nextval != curr_node or self.head.nextval != None):
            self.head.nextval = curr_node


    def print(self):
        while self.next != None :
            print("the printed tsructure is : ", self.value)


        """for index in range(0, self.level + 1):
            while(curr_node.next_level and curr_node.value < self.value):
                curr_node = curr_node.next
            print(curr_node.store)"""


list = skiplist(1,11)
list.insertNode(2)
list.insertNode(3)
list.print()
print(list.print())