class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    @property
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        return f'{self.queue}'
class MyStack:

    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        result = Queue()
        temp = Queue()
        for i in range(self.stack.size-1):
            temp.push(self.stack.pop())
        answer = self.stack.pop()
        for i in range(temp.size):
            result.push(temp.pop())
        self.stack = result
        return answer


    def top(self) -> int:
        result = Queue()
        temp = Queue()
        for i in range(self.stack.size-1):
            temp.push(self.stack.pop())
        answer = self.stack.pop()
        temp.push(answer)
        for i in range(temp.size):
            result.push(temp.pop())
        self.stack = result
        return answer

    def empty(self) -> bool:
        return self.stack.is_empty()
    def __repr__(self):
        return f'{self.stack}'