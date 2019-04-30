"""
QueueNetwork	                        A class that simulates a network of queues.
QueueNetwork.animate	                Animates the network as it’s simulating.
QueueNetwork.clear	                    Resets the queue to its initial state.
QueueNetwork.clear_data	                Clears data from all queues.
QueueNetwork.copy	                    Returns a deep copy of itself.
QueueNetwork.draw	                    Draws the network.
QueueNetwork.get_agent_data	            Gets data from queues and organizes it by agent.
QueueNetwork.get_queue_data	            Gets data from all the queues.
QueueNetwork.initialize	                Prepares the QueueNetwork for simulation.
QueueNetwork.next_event_description	    Returns whether the next event is an arrival or a departure and the queue the event is accuring at.
QueueNetwork.reset_colors	            Resets all edge and vertex colors to their default values.
QueueNetwork.set_transitions	        Change the routing transitions probabilities for the network.
QueueNetwork.show_active	            Draws the network, highlighting active queues.
QueueNetwork.show_type	                Draws the network, highlighting queues of a certain type.
QueueNetwork.simulate	                Simulates the network forward.
QueueNetwork.start_collecting_data	    Tells the queues to collect data on agents’ arrival, service start, and departure times.
QueueNetwork.stop_collecting_data	    Tells the queues to stop collecting data on agents.
QueueNetwork.transitions	            Returns the routing probabilities for each vertex in the graph.
"""

"""
class queueing_tool.network.QueueNetwork(g, q_classes=None, q_args=None, seed=None, colors=None, max_agents=1000, blocking='BAS', adjust_graph=True)

https://queueing-tool.readthedocs.io/en/latest/network.html

Parameters: 
            g:                  networkx.DiGraph, numpy.ndarray, dict, None, etc.       create a graph { adj list x edge list }
            q_classes:          dict (optional)                                         Define the edge the belong to which server
            q_args:             dict (optional)                                         Define the type of the queue server
            seed:               int (optional)                                          An integer used to initialize numpy’s psuedo-random number generator.
            colors:             dict (optional)
            max_agents:         int (optional, default: 1000)                           The maximum number of agents that can be in the network at any time.
            blocking:           {'BAS', 'RS'} (optional, default: 'BAS')
            adjust_graph:       bool (optional, default: True)
          
"""

import queueing_tool as qt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


g = nx.moebius_kantor_graph()
q_cl = {1: qt.QueueServer}

def arr(t): 
    return t + np.random.gamma(4, 0.0025)

def ser(t): 
    return t + np.random.exponential(0.025)





q_ar = {
    1: {
        'arrival_f': arr,
        'service_f': ser,
        'num_servers': 5
    }
}

net = qt.QueueNetwork(g, q_classes=q_cl, q_args=q_ar, seed=13)    


#To specify that arrivals enter from type 1 edges and simulate run:
########################################
net.initialize(edge_type=1)
net.simulate(n=100)


#Now we’d like to see how many agents are in type 1 edges:
###########################################################
for i in range(len(net.edge2queue)):
    data = net.edge2queue[i]
    print(data)
   

nA = [(q.num_system, q.edge[2]) for q in net.edge2queue if q.edge[3] == 1]
nA.sort(reverse=True)
print(nA[:5])



"""
To view the state of the network do the following (note, you need to have pygraphviz installed and your graph may be rotated):
"""

pos = nx.nx_agraph.graphviz_layout(g.to_undirected(), prog='neato') 
net.draw(pos=pos,fname='ee.png') 
plt.show()
