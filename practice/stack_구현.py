import queue


class Stack(object):
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, element):
        self.q1.put(element)

    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return self.q2.get()


if __name__ == '__main__':
    s = Stack()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    print(s.dequeue())
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
