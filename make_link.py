GRAPH = {}
def make_link(Graph, node1, node2):
    if node1 not in Graph:
        Graph[node1] = {}
    Graph[node1][node2] = 1
    if node2 not in Graph:
        Graph[node2] = {}
    Graph[node2][node1] = 1
    return Graph

filghts = []
filghts.append(("LAX","DFW"))
filghts.append(("SAE", "LAX"))
filghts.append(("ORD", "LAX"))
filghts.append(("ORD", "SAE"))

for (x,y) in filghts: print make_link(GRAPH, x, y)
