from stack import Stack


class Sweepstakes_stack_manager:
    def __init__(self):
        self.stack = Stack()
        self.name = 'stack manager'

    def insert_sweepstakes(self, sweepstakes):
        self.stack.push(sweepstakes)
        print(f"\nstack: {self.stack.stack}")

    def get_sweepstakes(self):
        self.stack.pop()
        print(f"\nstack: {self.stack.stack}")
