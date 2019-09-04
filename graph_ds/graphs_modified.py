# In previous example we represented each vertex of the graph with a Nodes class
# But the class has only a data attribute & nothing else.
# The class is basically an attribute, so use the data not as a Node.

from pprint import pprint


class Graph:
    def __init__(self):
        self.no_of_nodes = 0
        self.adj_list = {}

    def nodes_list(self):
        return self.adj_list.keys()

    def add_vertex(self, node):
        if node not in self.nodes_list():
            self.adj_list[node] = []
            self.no_of_nodes += 1
        else:
            print('Node already exists!')

    def add_edge(self, node1, node2):
        if node1 in self.nodes_list() and node2 in self.nodes_list():
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)

    def show_connections(self):
        for node, neighbours in self.adj_list.items():
            print(f'{node} \t --> \t ', end='')
            for neighbour in sorted(neighbours):
                print(f'{neighbour} \t ', end='')
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
pprint(g.adj_list, width=15)
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
pprint(g.adj_list, width=25)
print()
g.show_connections()

print()
g.add_vertex('0')
