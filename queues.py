# queues - a line of people waiting to be served
#        - linear data structure
#        - one can add item from the end  & remove item from the front
#        - FIFO
# Queues can be implemented using arrays or linked lists


class Queue:
    def __init__(self):
        self.queue = []

    def enque(self, data):
        self.queue.append(data)

    def deque(self):
        if len(self.queue) == 0:
            return
        dequeued = self.queue.pop(0)
        return dequeued


my_queue = Queue()

my_queue.enque('Person 1')
my_queue.enque('Person 2')
my_queue.enque('Person 3')
my_queue.enque('Person 4')
my_queue.enque('Person 5')

print(my_queue.queue)

removed_data = my_queue.deque()
print(f"Removed - {removed_data if removed_data is not None else 'No thing'}")
print(my_queue.queue)
