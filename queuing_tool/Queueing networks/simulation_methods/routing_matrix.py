import queueing_tool as qt


g = qt.generate_random_graph(5, seed=10)
net = qt.QueueNetwork(g)
mat = qt.generate_transition_matrix(g, seed=10)
net.set_transitions(mat)
net.transitions(False)  
print(net.transitions(True))

"""

[[0.         0.         1.         0.         0.        ]
 [0.         0.         0.53488372 0.46511628 0.        ]
 [0.53793103 0.02068966 0.         0.         0.44137931]
 [0.         1.         0.         0.         0.        ]
 [0.         0.         0.6        0.         0.4       ]]
 
"""
