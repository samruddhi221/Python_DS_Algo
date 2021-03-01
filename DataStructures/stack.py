class Stack:
    def __init__(self, size: int):
        self.size = size
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, element: int) -> None:
        if self.size == len(self.stack):
            print("stack overflow")
        else:
            self.stack.append(element)

    def pop(self) -> int:
        if self.is_empty():
            return 0
        else:
            element = self.stack[-1]
            self.stack.pop(-1)
            return element

    def peek_top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]

    def __str__(self):
        return f'{self.stack}'


if __name__ == '__main__':
    my_stack = Stack(10)
    my_stack.push(5)
    my_stack.push(7)
    my_stack.push(1)
    print(my_stack)
    top = my_stack.pop()
    print(top)
    print(my_stack)
    print(my_stack.peek_top())
    print(my_stack.is_empty())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())


