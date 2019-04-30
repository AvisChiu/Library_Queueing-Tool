import queueing_tool as qt
import networkx as nx
import matplotlib.pyplot as plt


def creat_network():
       g = qt.generate_random_graph(10, seed=3)
       q = qt.QueueNetwork(g, seed=3)
       q.max_agents = 20
       q.initialize(100)
       q.simulate(10000)

       pos = nx.nx_agraph.graphviz_layout(g.to_undirected(), prog='neato')
       scatter_kwargs = {'s': 30}
       q.draw(pos=pos, scatter_kwargs=scatter_kwargs, bgcolor=[0,0,0,0],
              figsize=(6, 6), fname='fig.png',
              bbox_inches='tight')


       plt.show()

if __name__ == "__main__":
     creat_network()