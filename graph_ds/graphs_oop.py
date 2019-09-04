# This is a graph representation of the picture in '2.exercise_graph.PNG'

from pprint import pprint


class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Node->{self.data}'


class Graph:
    def __init__(self):
        self.no_of_nodes = 0
        self.adj_list = {}

    def add_vertex(self, val):
        not_found = True
        for node in self.adj_list.keys():
            if node.data == val:
                not_found = False

        if not_found:
            new_node = Node(val)
            self.no_of_nodes += 1
            self.adj_list[new_node] = []
        else:
            print('\nNode already exists!')

    def add_edge(self, val1, val2):
        node1 = node2 = None
        for node in self.adj_list.keys():
            if node.data == val1:
                node1 = node
            elif node.data == val2:
                node2 = node

        if (node1 is not None) and (node2 is not None):
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)

    def show_connections(self):
        for node, neighbours in self.adj_list.items():
            print(f'{node.data} \t--> \t', end='')
            for neighbour in neighbours:
                print(f'{neighbour.data} \t', end='')
            print()


g = Graph()


g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')

print('\nBefore Insertion')
print('----------------')
pprint(g.adj_list)
print()
g.show_connections()

g.add_edge('3', '1')
g.add_edge('3', '4')
g.add_edge('4', '2')
g.add_edge('4', '5')
g.add_edge('1', '2')
g.add_edge('1', '0')
g.add_edge('0', '2')
g.add_edge('6', '5')

print('\nAfter Insertion')
print('---------------')
pprint(g.adj_list)
print()
g.show_connections()

g.add_vertex('0')