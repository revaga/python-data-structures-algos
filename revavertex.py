class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.previous = None

    def getVerticeID(self):
        return self._id

    def getWeight(self, neighbor):
        return self._adjacent[neighbor]


    def getDistance(self):
        return self._distance


    def getConnections(self):
        self._adjacent.keys()

    def setDistance(self, distance):
        self.distance = distance

    def setPrevious(self, previous):
        self._previous = previous

    def addNeighbor(self, weight, neighbor):
        self._adjacent[neighbor] = weight


    def __str__(self):
        return str(self._id) + ' adjacent: ' + str([x.id for x in self._adjacent])