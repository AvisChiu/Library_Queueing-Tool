"""
A finite capacity queue.

If an agent arrives to a queue that is at capacity, then the agent gets blocked. 
If this agent is arriving from inside the network then that agent has to stay at their current queue. 
If the agent is arriving from outside the network then the agent is deleted.

"""

"""
another type of server, named Loss server     

default_classes = {
... 0: qt.NullQueue,
... 1: qt.QueueServer,
... 2: qt.LossQueue,
... 3: qt.LossQueue,
... 4: qt.LossQueue
... }

the setting of QueueServer:

def __init__(self, num_servers=1, arrival_f=None,
                 service_f=None, edge=(0, 0, 0, 1),
                 AgentFactory=Agent, collect_data=False, active_cap=infty,
                 deactive_t=infty, colors=None, seed=None,
                 coloring_sensitivity=2, **kwargs):

the setting of LossServer: 

def __init__(self, qbuffer=0, **kwargs):

        super(LossQueue, self).__init__(**kwargs)
        self.num_blocked = 0
        self.buffer = qbuffer

the setting of InfoServer:

"""



import queueing_tool as qt
import numpy as np


m = qt.queues.LossQueue() 
print("\nAnother type of server : LossQueue ")
print(m)
print("the capacity of server: ",m.at_capacity(),"\n")

   