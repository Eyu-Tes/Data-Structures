# stacks - plates piled on top of each other
#        - linear data structure
#        - one can add or remove plates only from the top
#        - LIFO

# Stacks can be implemented using arrays or linked lists


# When implementing stacks with linked lists, we only need pointer to top item
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node->{self.data}'


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        popped_item = None
        if self.top is None:
            pass
        else:
            popped_item = self.top
            self.top = self.top.next

        return popped_item


stack = Stack()
stack.push('google')
print(stack.peek())
stack.push('youtube')
print(stack.peek())
stack.pop()
print(stack.peek())
