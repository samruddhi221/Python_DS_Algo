class Queues:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * self.size
        self.start = 0
        self.end = 0

    def add(self, element: int):
        if self.end == self.size:
            print("Queue is full")
        else:
            self.queue[self.end] = element
            self.end += 1

    def remove(self):
        if self.is_empty():
            print("Queue is empty, can't remove the element.")
        else:
            self.queue[self.start] = None
            self.start += 1

    def peek(self) -> int:
        if not self.is_empty():
            return self.queue[self.start]
        else:
            print("queue is empty")

    def is_empty(self) -> bool:
        return self.start == self.end


if __name__ == '__main__':
    my_queue = Queues(5)
    my_queue.add(3)
    my_queue.add(4)
    my_queue.add(5)
    my_queue.add(9)
    my_queue.add(2)
    my_queue.add(1)
    print(my_queue.peek())
    my_queue.remove()
    my_queue.remove()
    my_queue.remove()
    my_queue.remove()
    my_queue.remove()
    my_queue.remove()
    my_queue.peek()