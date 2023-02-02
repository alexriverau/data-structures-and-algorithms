class Graph:

    def __init__(self):
        self.vertices = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.vertices[vertex] = []  # sets key to vertex, and its value to an empty list
        return vertex

    def add_edge(self, v1, v2, weight=None):
        if v1 in self.vertices and v2 in self.vertices:
            if v1.value == v2.value:
                self.vertices[v1].append(Edge(v2, weight))
            else:
                self.vertices[v1].append(Edge(v2, weight))
                self.vertices[v2].append(Edge(v1, weight))
        else:
            raise KeyError

    def get_nodes(self):
        if self.vertices:
            return set(self.vertices)
        else:
            return set()

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []

    def size(self):
        return len(self.vertices)


class Vertex:

    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
