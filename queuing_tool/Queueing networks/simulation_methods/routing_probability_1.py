import queueing_tool as qt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


g = qt.generate_random_graph(5, seed=10)                # 5 nodes network
net = qt.QueueNetwork(g)
net.transitions(False)

print(net.transitions(True))                            # shown as a matrix
print(net.transitions(False))                           # shown as a dictionary


"""
the probability will be changed if the seed is changed
"""