
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

        # A utility function to find set of an element i

    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

        # A function that does union of two sets of x and y

    def has_cycle(self):
        visited_vertices = []
        for g in self.graph:
            if g[0] not in visited_vertices:
                visited_vertices.append(g[0])
                break
        for g in self.graph:
            if g[0] in visited_vertices:
               if g[1] not in visited_vertices:
                    visited_vertices.append(g[1])
               else:
                   return True
        return  False



g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

print(g.has_cycle())

# g.KruskalMST()
