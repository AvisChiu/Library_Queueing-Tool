import queueing_tool as qt
import matplotlib.animation as manimation
from matplotlib import *



g = qt.generate_pagerank_graph(4, seed=13)
net = qt.QueueNetwork(g, seed=13)
net.initialize()
net.animate(figsize=(4, 4)) 



kwargs = {
    'filename': 'test.mp4',
    'frames': 300,
    'fps': 30,
    'writer': 'mencoder',
    'figsize': (4, 4),
    'vertex_size': 15
}

"""
This method calls FuncAnimation and optionally matplotlib.animation.FuncAnimation.save(). 
Any keyword that can be passed to these functions are passed via kwargs.
"""
net.animate(**kwargs) 


