import revagraph
import revavertex

test = revagraph.Graph()
test.addVertex("a")
test.addVertex("b")
test.addVertex("c")
test.addVertex("d")
test.addEdge("a", "b", 4)
test.addEdge("a", "c", 1)
test.addEdge("b", "a", 3)
test.addEdge("b", "d",2)
test.addEdge("c", "a", 1)
test.addEdge("c", "b", 5)

