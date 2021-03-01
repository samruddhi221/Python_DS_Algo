class MyCircularQueue:
    def __init__(self, size: int):
        self.capacity = size
        self.queue = [-1] * size
        self.start = -1
        self.end = -1

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        else:
            if self.is_empty():
                self.start = 0
                self.end = 0
            else:
                self.end = (self.end + 1) % self.capacity
            self.queue[self.end] = value
            return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        if self.end == self.start:  # only one element is remaining in the queue
            self.queue[self.start] = -1
            self.start = -1
            self.end = -1
        else:
            self.queue[self.start] = -1
            self.start = (self.start + 1) % self.capacity
        return True

    def front(self) -> int:
        if self.start != -1:
            # self.start = (self.start + 1) % self.capacity
            return self.queue[self.start]
        else:
            return -1

    def rear(self) -> int:
        if self.end != -1:
            return self.queue[self.end]
        else:
            return -1

    def is_empty(self) -> bool:
        if self.start == -1 and self.end == -1:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if ((self.end + 1) % self.capacity) == self.start:
            return True
        else:
            return False

    def __str__(self):
        return f'Queue: {self.queue}, front_ptr: {self.start}, rear_ptr: {self.end}'


if __name__ == '__main__':
    ring_buffer = MyCircularQueue(5)
    ring_buffer.enqueue(8)
    ring_buffer.enqueue(2)
    ring_buffer.enqueue(3)
    print(ring_buffer.front(), ring_buffer.rear())
    ring_buffer.enqueue(1)
    ring_buffer.enqueue(9)
    print(ring_buffer)
    ring_buffer.enqueue(5)
    ring_buffer.dequeue()
    ring_buffer.dequeue()
    print(ring_buffer)
    ring_buffer.enqueue(4)
    print(ring_buffer)
    ring_buffer.dequeue()
    ring_buffer.dequeue()
    print(ring_buffer.front(), ring_buffer.rear())
    ring_buffer.dequeue()
    ring_buffer.dequeue()
    ring_buffer.dequeue()
