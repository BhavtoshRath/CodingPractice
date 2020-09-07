# Enqueue from rear, dequeue from front.


class queue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity - 1

        self.size = 0
        self.capacity = capacity

        self.Q = [None] * capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def Enqueue(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item

        self.size += 1

    def Dequeue(self):
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def q_front(self):
        return self.Q[self.front]

    def q_rear(self):
        return self.Q[self.rear]


queue = queue(30)
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
queue.Dequeue()
queue.q_front()
queue.q_rear()