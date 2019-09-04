# linked lists - many individual boxes connected by strings
#              - linear data structure


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node -> {self.data}'


class SLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node, end=", \t")
            current_node = current_node.next
        print()

    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)
        current_node = self.head

        if current_node is None:
            self.head = new_node
            return

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def insert_middle(self, new_data, insert_after):
        current_node = self.head
        node_found = False
        while current_node is not None:
            if current_node.data == insert_after:
                node_found = True
                break
            current_node = current_node.next
        if not node_found:
            print('Node is absent.')
            return

        new_node = Node(new_data)
        current_node = self.head
        while current_node.data != insert_after:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        try:
            current_node = self.head
            while current_node is not None:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next
                    break
                current_node = current_node.next
        except AttributeError:
            print('Node is absent.')


# Creation
linked_list = SLinkedList()
linked_list.head = Node('Mon')
n2 = Node('Tue')
n3 = Node('Wed')
linked_list.head.next = n2
n2.next = n3

# Traversal
linked_list.traverse()

# Insertion
# ---------
# Beginning
linked_list.insert_beginning('Sun')
linked_list.traverse()

# End
linked_list.insert_end('Thu')
linked_list.traverse()

# Middle
linked_list.insert_middle('EYU', 'Tue')
linked_list.traverse()

# Deletion
# --------
linked_list.remove('EYU')
linked_list.traverse()
linked_list.remove('July')

# Delete all
linked_list.head = None
linked_list.traverse()
print('--------------')