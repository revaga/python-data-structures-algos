import revavertex


class Graph:
    def __init__(self):
        self.vertDictionary = None
        self.numVertices = 0

    def getVertex(self, label):
        if label in self.vertDictionary:
            return label
        else:
            return None

    def getVertices(self):
        return self.vertDictionary.keys()

    def addVertex(self, node):
        self.numVertices += 1
        newVertex = revavertex.Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def addEdge(self, previous, post, weight):
        self.vertDictionary[previous].addNeighbor(self.vertDictionary[post], weight)

    def setPrevious(self, node, previous):
        self.vertDictionary[node].setPrevious(previous)

#def iterate(self):

#def getEdges(self):
