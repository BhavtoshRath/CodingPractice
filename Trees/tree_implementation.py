class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data) #recursive call
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data # If this is the first node in the tree.


    def find(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.find(data)
        else:
            return True


    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()





    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()





root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find(7))
print(root.find(14))
root.inorder()