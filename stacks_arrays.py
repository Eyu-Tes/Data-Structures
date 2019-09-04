# stacks - plates piled on top of each other
#        - linear data structure
#        - one can add or remove plates only from the top
#        - LIFO

# Stacks can be implemented using arrays or linked lists


# When implementing stacks with arrays, we can use the index to get top item
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return
        popped = self.stack.pop()
        return popped

    def peek(self):
        if len(self.stack) == 0:
            return 'Stack is empty'
        return self.stack[-1]


stack = Stack()
stack.push('google')
print(stack.peek())
stack.push('youtube')
print(stack.peek())
stack.pop()
print(stack.peek())







