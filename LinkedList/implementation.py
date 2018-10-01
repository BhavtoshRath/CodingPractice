class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):  # 'head' is a pointer, not a node!!!
        node = Node(data)
        node.setNext(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        while current.getNext() != None:
            if current.getData() == data:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, data):
        current = self.head
        previous = None
        while current.getNext():
            if current.getData() == data and previous is None:
                self.head = current.getNext()
                return True
            elif current.getData() == data and previous is not None:
                previous.setNext(current.getNext())
                return True
            else:
                previous = current
                current = current.getNext()
        return False

    def append(self, data):
        node = Node(data)
        current = self.head
        while current.getNext():
            current = current.getNext()
        current.setNext(node)







mylist = LinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(7)
mylist.add(727)

# print(mylist.size())
# print(mylist.search(77))
# print(mylist.remove(77))
mylist.append(21)
print(mylist)