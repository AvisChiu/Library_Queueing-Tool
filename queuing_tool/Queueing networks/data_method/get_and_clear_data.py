import queueing_tool as qt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

"""
Data is not collected by default. Before simulating, by sure to turn it on (as well as initialize the network). 
The following returns data from queues with edge_type 1 or 3:


out : :class:`~numpy.ndarray`
            * 1st: The arrival time of an agent.
            * 2nd: The service start time of an agent.
            * 3rd: The departure time of an agent.
            * 4th: The length of the queue upon the agents arrival.
            * 5th: The total number of :class:`Agents<.Agent>` in the
              :class:`.QueueServer`.
            * 6th: The :class:`QueueServer's<.QueueServer>` edge index.

[[18.85401922 18.85401922 19.43420878  0.          1.          0.        ]
 [11.15107268 11.15107268 12.09497275  0.          1.          4.        ]
 [15.31835177 15.31835177 15.59703253  0.          1.          4.        ]
 [22.36394966 22.36394966  0.          0.          1.          4.        ]
 [22.46700843  0.          0.          1.          2.          4.        ]]

"""
g = qt.generate_pagerank_graph(100, seed=13)
net = qt.QueueNetwork(g, seed=13)
net.start_collecting_data()

net.initialize(10)
net.simulate(2000)

# pos = nx.nx_agraph.graphviz_layout(g.to_undirected(), prog='neato') 
# net.draw(pos=pos,fname='pagerank_graph.png') 
# plt.show()

print("============all queue data=============")
data = net.get_queue_data()
print("total number of queue data: ",len(data),"\n")


"""
根據edge的類型查看數據
"""
print("===========according to the edge type(e.g. type 1)==============")
data1 = net.get_queue_data(edge_type=(1))
print("total number of type 1 queue: ",len(data1))
data2 = net.get_queue_data(edge_type=(2))
print("total number of type 2 queue: ",len(data2))
data3 = net.get_queue_data(edge_type=(3))
print("total number of type 3 queue: ",len(data3),"\n")
# data3 = net.get_queue_data(edge_type=(1,3))




# To get data from an edge connecting two vertices do the following:
# If want to know all the edge of the graph. transition matrix is a good choice -----> net.transitions(False) 
print("=========According to the edge (e.g. 1-->50)================")   
data = net.get_queue_data(edge=(1,50))
print(data)



# You can specify the edge indices as well:
print("============queue no.4 data=============")
data = net.get_queue_data(queues=(4))
print("queue no.4 data: \n",data,"\n")
print("============queue no.0 data=============")
data = net.get_queue_data(queues=(0))
print("queue no.0 data: \n",data,"\n")



print("===========clear queue no.4 data==============\n")
net.clear_data(queues=4, edge=None, edge_type=None)    # queue 標識爲 4 的全部清除 (其實就是根據哪一個類型來刪除數據~~！！！)
data = net.get_queue_data(queues=(4)) 
print("queue no.0 data: \n",data,"\n")





