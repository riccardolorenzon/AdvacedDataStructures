## Examine the Graph

## Now that we can create a Graph/Network
## data structure, we need to work on
## understanding the graph.

## Lets see how many nodes are connected
## together. -- Connected Nodes
GRAPH = {}

def make_link(Graph, node1, node2):
    """
    A Graph will be a dictionary containing nodes.
    Theses nodes will be a dictionary of neighbour nodes.
    The node's dict. key will be the neighbour node and
    it's value will be 1.
    Return the updated Graph.
    """
    if node1 not in Graph:
        Graph[node1] = {}
    (Graph[node1])[node2] = 1
    if node2 not in Graph:
        Graph[node2] = {}
    (Graph[node2])[node1] = 1
    return Graph

connected_letters = [('a','g'),('a','d'),('d','g'),('g','c'), \
           ('b','f'),('f','e'),('e','h')]

for (x,y) in connected_letters: make_link(GRAPH, x, y)

#####################################################################

def marked_node(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbour in G[node]:
        if neighbour not in marked:
            total_marked += marked_node(G, neighbour, marked)
    return total_marked

def list_node_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print "Graph containing", node, \
                  ":", marked_node(G, node, marked)

##########################
### Pairwise Connection Homework
##########################

def is_connected(G, node1, node2):
    ## Your Code Here
    marked = {}
    marked_node(G, node1, marked)
    return node2 in marked

#list_node_sizes(GRAPH)
print is_connected(GRAPH, 'a','h')


