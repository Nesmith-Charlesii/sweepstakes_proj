class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        # stack is last in, first out
        return self.stack.pop(-1)
