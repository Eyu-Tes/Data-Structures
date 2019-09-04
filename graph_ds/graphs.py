# graphs - network
#        - a tree in which child nodes can have more than 1 parent node

# ------------ Directed Acyclic Graph (DAG) ---------------------
# A graph that is directed and without cycles connecting the other edges.
# i.e, it is impossible to traverse the entire graph starting at one edge.
# The edges of the directed graph only go one way.
# Applied to problems related to:
#                                - data processing,
#                                - scheduling,
#                                - finding the best route in navigation, &
#                                - data compression.

# This is a graph representation of the picture in '1.exercise_graph.PNG'


from pprint import pprint

vertices = [0, 1, 2, 3]
print('\nvertices')
print(vertices)

# Adjacency List
adj_list = {0:[2], 1:[2,3], 2:[0,1,3], 3:[1,2]}
print('\nAdjacency List')
pprint(adj_list)

# Edge List
# Uses Adjacency List to obtain adjacent vertices
edge_list = []
for vertex in adj_list.keys():
    neighbours = adj_list.get(vertex)
    for neighbour in neighbours:
        edge_list.append((vertex, neighbour))

print('\nEdge List')
pprint(edge_list)

# Adjacency Matrix
# Uses a combination of Vertices & Edge List
rows = cols = len(adj_list.keys())
adj_matrix = [[0 for y in range(cols)] for x in range(rows)]

print('\nAdjacency Matrix')
print('Before Fill')
pprint(adj_matrix, width=15)

for edge in edge_list:
    x = vertices.index(edge[0])
    y = vertices.index(edge[1])
    adj_matrix[x][y] = 1

print('\nAfter Fill')
pprint(adj_matrix, width=15)