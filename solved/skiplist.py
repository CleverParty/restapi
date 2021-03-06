from __future__ import absolute_import, print_function

import os
import sys
import math
from random import gauss


def printit(curr_node):
    while curr_node.nextval != None :
        print("the values are :\n",curr_node.store)

class Node(object):
    name  = ""
    def __init__(self, level , store):
        self.name = 'Node'
        self.store = store
        # self.next_level = None
        self.level = level
        self.nextval = None

    def printStore(self):

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
        print("the value in this node is : ",self.level)

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
        for index in range(0, self.level + 1):
            while(curr_node.nextval and curr_node.value < self.value):
                curr_node = curr_node.nextval
            print("the value of the index is :",index)
            if(curr_node.nextval == None ):
                print("reached end of list")

    def printValues

node_test = Node(1,18)
list = skiplist(1,10)
print(list.printvalue())
list.insertNode(2)
list.insertNode(3)
head = list.create(1,19)
printit(head)
