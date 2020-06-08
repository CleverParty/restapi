import sys

class Node(object):
    name  = ""
    def __init__(self, store):
        self.name = 'Node'
        self.store = store
        self.parent = None
        # self.next_level = None
        self.left = None
        self.right = None
        self.color = 1 # 1 - red , 0 - black


    def printValue(self):
        print("the value is :{}".format(self.store))


class redblack():
    name = "redblack"
    def __init__(self):
        self.obj = Node(0)
        self.color = 0 
        self.right = None
        self.left = None
        self.root = self.obj
    
    def preorder(self, node):
        if node != None:
            sys.stdout.write(str(node.store) + " ")
            self.preorder(node.left)
            self.preorder(node.right)
    
    def print_preorder(self):
        self.preorder(self.root)

    def insert(self , payload):
        temp = Node(payload)
        temp.parent = None
        temp.store = payload
        temp.left = None
        temp.right = None
        temp.color = 1
        swapednode = None
        x = self.root

        while x != None:
            swapednode = x
            if temp.store < x.store:
                x = x.left
            else:
                x = x.right

        temp.parent = swapednode
        if swapednode == None:
            self.root = temp
        elif temp.store < swapednode.store:
            swapednode.left = temp
        else:
            swapednode.right = temp

        if temp.parent == None:
            temp.color = 0 # black node to be placed here
            return

        if temp.parent.parent == None:
            return

rb = redblack()
rb.insert(1)
rb.insert(23)
rb.insert(90)
rb.print_preorder()