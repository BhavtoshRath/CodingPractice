class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, new_data):
        self.data = new_data

    def getData(self):
        return self.data

    def setNext(self, new_next):
        self.next = new_next

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = Node(new_data)
        new_node.setNext(self.head)
        self.head = new_node

    def kToLast(self, k):
        temp = []
        l = 0
        current = self.head
        while current:
            l += 1
            if l >= k:
                temp.append(current.getData())
            current = current.getNext()

        return temp





mylist = LinkedList()
mylist.add(8)
mylist.add(9)
mylist.add(10)
mylist.add(11)
print(mylist.kToLast(3))

print('x')