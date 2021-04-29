from queue import Queue


class Sweepstake_queue_manager:
    def __init__(self):
        self.queue = Queue()
        self.name = 'queue manager'

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue(sweepstakes)
        print(self.queue.queue)

    def get_sweepstakes(self):
        self.queue.dequeue()
        print(self.queue.queue)
