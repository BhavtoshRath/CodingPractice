class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = temp
            self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next #*

        if self.front is None:
            self.rear = None
        return str(temp.data)


q = Queue()
q.EnQueue(1)
q.EnQueue(2)
q.DeQueue()
q.DeQueue()
q.EnQueue(3)
q.EnQueue(4)
q.EnQueue(5)


























































