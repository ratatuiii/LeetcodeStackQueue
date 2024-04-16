class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop(-1)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    @property
    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return f'{self.stack}'
class MyQueue:
    def __init__(self):
        self.queue = Stack()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        result = Stack()
        temp = Stack()
        for i in range(self.queue.size-1):
            temp.push(self.queue.pop())
        answer = self.queue.pop()
        for i in range(temp.size):
            result.push(temp.pop())
        self.queue = result
        return answer

    def peek(self) -> int:
        result = Stack()
        temp = Stack()
        for i in range(self.queue.size-1):
            temp.push(self.queue.pop())
        answer = self.queue.pop()
        temp.push(answer)
        for i in range(temp.size):
            result.push(temp.pop())
        self.queue = result
        return answer

    def empty(self) -> bool:
        return self.queue.is_empty()
    def __str__(self):
        return f'{self.queue}'