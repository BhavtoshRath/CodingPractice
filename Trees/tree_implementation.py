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
            self.data = data # If this is the same as node in the tree.

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

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)



l = [1,2,3,4]


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find(7))
print(root.find(14))
print('root.inorder()')
print(root.inorder())
print('root.postorder()')
print(root.postorder())