class Queue:

    def __init__(self, max_size: int = None):
        """
        Creating queues with lists.
        TODO : Implement queues with singly LinkedLists
        """
        self.max_size = max_size
        self.queue_size = max_size or 0
        self.queue_ds = [None] * self.queue_size

    def _enque(self, value: int):
        if (self.max_size and len(self.queue_ds) < self.max_size)\
                or not self.max_size:
            ind = len(self.queue_ds) - 1
            self.queue_ds[ind] = value
        elif self.max_size and len(self.queue_ds) == self.max_size:
            print("Cannot add anymore values as queue is full. Adjust the queue size.")

    def _deque(self):
        if len(self.queue_ds) > 0:
            self.queue_ds.remove(self.queue_ds[0])
        elif len(self.queue_ds) == 0:
            print("Cannot remove anymore values as queue is empty.")
