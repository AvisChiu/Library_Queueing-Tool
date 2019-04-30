"""
Returns the routing probabilities for each vertex in the graph.

Parameters:	
            return_matrix : bool (optional, the default is True)


Specifies whether an ndarray is returned. If False, a dict is returned instead.

Returns:	
out : a dict or ndarray

The transition probabilities for each vertex in the graph. 
If out is an ndarray, then out[v, u] returns the probability of a transition from vertex v to vertex u. 
If out is a dict then out_edge[v][u] is the probability of moving from vertex v to the vertex u.

"""

import queueing_tool as qt
import networkx as nx

g = nx.sedgewick_maze_graph()
net = qt.QueueNetwork(g)

mat = qt.generate_transition_matrix(g, seed=96)
net.set_transitions(mat)\

print(qt.graph2dict(g, False))          # adjacency
print(net.transitions(True) ) 

