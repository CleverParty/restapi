from __future__ import absolute_import, print_function

import os
import sys
import math
from random import randint

class Node(object):
    name  = ""
    def __init__(self, key , level):
        self.name = 'name'
        self.key = key
        self.next_level = [None]*(level+1)
        self.level = level

class skiplist(object):
    name = ""
    def __init__(self,value,max):
        self.name = 'inner'
        self.max = max
        self.value = value
        self.level = 0

    def create(self, level , key):
        obj = Node(level,key)
        return obj
    def randomize(self):
        value = randint(int(self.level) - 1, int(self.max) - 1)


node_a = Node(1,1)
list = skiplist(1,10)
list.create(1,1)