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

    def insert_after_node(self, data1, data2):
        node = Node(data1)
        current = self.head
        while current.getNext():
            if current.getData() != data2:
                current = current.getNext()
            else:
                node.setNext(current.getNext())
                current.setNext(node)
                return True
        return False

    def insert_before_node(self, data1, data2):
        node = Node(data1)
        current = self.head
        previous = None
        while current.getNext():
            if current.getData() == data2 and previous is None:
                node.setNext(current)
                return True
            if current.getData() == data2 and previous is not None:
                node.setNext(current)
                previous.setNext(node)
                return True
            else:
                previous = current
                current = current.getNext()
        return False

    def RemDups(self):  # Works only if there are two repetitions
        previous = self.head
        current = previous.getNext()

        while previous.getNext() is not None:
            if previous.getData() == current.getData():
                previous.setNext(current.getNext())
                return True
            previous = current
            current = current.getNext()




mylist = LinkedList()
mylist.add(8)
mylist.add(8)
mylist.add(9)
mylist.add(7)

mylist.RemDups()
print(mylist)






























































