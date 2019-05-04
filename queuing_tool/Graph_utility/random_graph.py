import queueing_tool as qt
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


pTypes = {1: 0.5, 2: 0.25, 3: 0.25}
g = qt.generate_random_graph(10, proportions=pTypes, seed=17)
non_loops = [e for e in g.edges() if e[0] != e[1]]
p1 = np.sum([g.ep(e, 'edge_type') == 1 for e in non_loops])
float(p1) / len(non_loops) 

p2 = np.sum([g.ep(e, 'edge_type') == 2 for e in non_loops])
float(p2) / len(non_loops) 

p3 = np.sum([g.ep(e, 'edge_type') == 3 for e in non_loops])
float(p3) / len(non_loops) 

nx.draw_networkx(g)
plt.axis('off')
plt.show()


"""
undirected graph (parameters: is_directed=False)
"""
# p = np.random.rand(4)
# p = p / sum(p)
# p = {k + 1: p[k] for k in range(4)}
# g = qt.generate_random_graph(num_vertices=10, is_directed=False, proportions=p)
# nx.draw_networkx(g)
# plt.axis('off')
# plt.show()


