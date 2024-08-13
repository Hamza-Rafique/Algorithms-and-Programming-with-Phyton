class StackList:
        
    # def __init__(self):
    items = [1, 2, 3, 4, 5]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
         if not self.isEmpty():
            return self.items[len(self.items) - 1]
         else:
            return None

        # return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

my_stack = StackList()

print(my_stack.isEmpty())

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.isEmpty())

print(my_stack.peek())
print(my_stack.size())

my_stack.pop()

print(my_stack.peek())
print(my_stack.items)
