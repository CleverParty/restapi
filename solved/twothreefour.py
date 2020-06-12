import numpy as np 

class two:
    def __init__(self,first=1,second=2):
        print("the two node init")
        self.first = first  
        self.second = second
    def print(self):
        print("values stored are : {first} and {second} ".format(first = self.first, second = self.second))

class three:
    def __init__(self):
        print("the three node init")

class four:
    def __init__(self):
        print("the four node init")


check=two(1,2)
check.print()

