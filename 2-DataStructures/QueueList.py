class QueueList:
    def __init__(self):
        self.items = []  # [1, 2, 3, 4, 5]

    def isEmpty(self):
        return self.items == [] # [1, 2, 3, 4, 5] == []

    def enqueue(self, item):
        self.items.insert(0, item) # [5, 4, 3, 2, 1] insert(0, item) = [item, 5, 4, 3, 2, 1] 

    def dequeue(self):
        return self.items.pop() # [5, 4, 3, 2, 1] pop() = [5, 4, 3, 2]

    def size(self):
        return len(self.items) # [5, 4, 3, 2, 1] len() = 5

    def peek(self):
        return self.items[len(self.items) - 1] # [5, 4, 3, 2, 1] len() = 5

    def __str__(self):
        return str(self.items) # [5, 4, 3, 2, 1] str() = [5, 4, 3, 2, 1]

    def __repr__(self):
        return str(self) # [5, 4, 3, 2, 1] str() = [5, 4, 3, 2, 1]
    
my_queue = QueueList()

print(my_queue.isEmpty())

my_queue.enqueue(1) # [1]
my_queue.enqueue(2) # [1, 2]
my_queue.enqueue(3) # [1, 2, 3]
print(my_queue.isEmpty()) # [1, 2, 3] isEmpty() = False

print(my_queue.peek()) # [1, 2, 3] peek() = 3
print(my_queue.size()) # [1, 2, 3] size() = 3

my_queue.dequeue() #  [2, 3]
print(my_queue.peek()) # [2, 3] peek() = 2
print(my_queue.items) # [2, 3] items = [2, 3]
