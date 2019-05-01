"""

Parameters:	
                update_colors : bool (optional, default: True).

                Specifies whether all the colors are updated.

                line_kwargs : dict (optional, default: None)        Any keyword arguments accepted by LineCollection

                scatter_kwargs : dict (optional, default: None)     Any keyword arguments accepted by scatter().

                bgcolor : list (optional, keyword only)             A list with 4 floats representing a RGBA color. The default is defined in self.colors['bgcolor'].

                figsize : tuple (optional, keyword only, default: (7, 7))       The width and height of the canvas in inches.



**kwargs

Any parameters to pass to QueueNetworkDiGraph.draw_graph().

"""


import queueing_tool as qt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


g = qt.generate_pagerank_graph(10, seed=13)
net = qt.QueueNetwork(g, seed=13)
net.initialize(100)
net.simulate(1200)

# net.draw(fname="state.png",line_kwargs={'linestyle': 'dashed'}) 
# net.draw(fname="state.png", scatter_kwargs={'s': 100}) 

fname = 'edge_type_2.png'
net.show_type(2, fname=fname) 

plt.show()