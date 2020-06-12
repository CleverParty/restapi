class Node:
    def __init__(self):
        self.next = [None]*26 # for each character possible (alphabet)
        self.last = False

class Trielist:
    def __init__(self):
        self.root = Node()
    
    def ordVal(self,val):
        return ord(val)-ord('a')
    
    def Insert(self,val):
        temp = self.root
        length = len(val)
        for i in range(length):
            storedchar = self.ordVal(val[i])
            if not temp.next[storedchar]:
                temp.next[storedchar] = Node()   # created a new node if no character with the same value exists in the list
            temp.next[storedchar] = temp

        temp.last = True

values = ["aba","abba","acca"]
trie = Trielist()
for key in keys:
    trie.Insert(key)