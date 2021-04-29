from sweepstake import Sweepstake
from queue import Queue


class Sweepstake_queue_manager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstakes):
        self.queue.enqueue()

    def get_sweepstakes(self):
        self.queue.dequeue()
