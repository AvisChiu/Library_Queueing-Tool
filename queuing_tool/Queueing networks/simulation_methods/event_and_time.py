"""
Let net denote your instance of a QueueNetwork. Before you simulate, 
you need to initialize the network, which allows arrivals from outside the network. 
To initialize with 2 (random chosen) edges accepting arrivals run:


Simulates the network forward.
Simulates either a specific number of events or for a specified amount of simulation time.

QueueNetwork.simulate(n=1, t=None)

        Parameters:	
                    n : int (optional, default: 1)          The number of events to simulate. If t is not given then this parameter is used.

                    t : float (optional)                    The amount of simulation time to simulate forward. If given, t is used instead of n.

"""

import queueing_tool as qt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def event():

    net.simulate(50000)                                         # set 50000 events
    net.num_events
    print("Number of events: ",net.num_events)


def time():
    
    t0 = net.current_time
    net.simulate(t=75)
    t1 = net.current_time
    result = t1-t0
    print("current time: ",t0)
    print("current time: ",t1)
    print("Simulation Time: ",result)

"""
conclusion: there are two kind of simulation method.
Event / Time

"""

if __name__ == "__main__":

    g = qt.generate_pagerank_graph(100, seed=50)                # 100 nodes
    net = qt.QueueNetwork(g, seed=50)
    net.initialize(2)   
    event()
    time()

