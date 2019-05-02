"""
            Agent	                                 The base class for an agent.
            InfoAgent	                             An agent that carries information about the QueueNetwork around.
            InfoQueue	                             A queue that stores information about the network.
            GreedyAgent	                             An agent that chooses the queue with the shortest line as their next destination.
            LossQueue	                             A finite capacity queue.
            NullQueue	                             A terminal queue.
            poisson_random_measure	                 A function that returns the arrival time of the next arrival for a Poisson random measure.
            QueueServer	                             The base queue-server class.
            ResourceAgent	                         An agent designed to interact with the ResourceQueue class.
            ResourceQueue	                         An queue designed to interact with the ResourceAgent class.

"""
# class queueing_tool.queues.QueueServer(
#     num_servers=1, 
#     edge=(0, 0, 0, 1), 
#     arrival_f=lambda t: t + np.random.exponential(1), 
#     service_f=lambda t: t + np.random.exponential(0.9), 
#     AgentFactory=Agent, 
#     keep_data=False, 
#     active_cap=np.infty, 
#     deactive_t=np.infty, 
#     coloring_sensitivity=2, 
#     **kwargs)

"""
Parameters:	

        num_servers : int or numpy.infty (optional, default: 1)                             The number of servers servicing agents.
        arrival_f : function (optional, default: lambda t: t + exponential(1))              A function that returns the time of next arrival from outside the network. When this function is called, t is always taken to be the current time.
        service_f : function (optional, default: lambda t: t + exponential(0.9))            A function that returns the time of an agent’s service time. When this function is called, t is the time the agent is entering service.
        edge : 4-tuple of int (optional, default: (0, 0, 0, 1))                             A tuple that uniquely identifies which edge this queue lays on and the edge type. 

                                                                                            The first slot of the tuple is the source vertex, the second slot is the target vertex, and the third slot is the edge_index of that edge, 
                                                                                            and the last slot is the edge type for this queue. This is automatically created when a QueueNetwork instance is created.

        AgentFactory : class (optional, default: the Agent class)                           Any function that can create agents. Note that the function must take one parameter.
        active_cap : int (optional, default: infty)                                         The maximum number of arrivals the queue will accept from outside the network.
        deactive_t : float (optional, default: infty)                                       Sets a stopping time, after which no more arrivals (from outside the network) will attempt to enter the QueueServer.
        collect_data : bool (optional, default: False)                                      A bool that defines whether the queue collects each Agent's arrival, service start, and departure times and other data. 
                                                                                            See fetch_data() for more on the information that is collected.
                                                                                            
        colors : dict (optional)                                                            A dictionary of the colors used when drawing the graph. The possible colors are:
            ----edge_loop_color                                                                     The default color of the edge if the edge is a loop.
            ----edge_color                                                                          The normal color a non-loop edge.
            ----vertex_fill_color                                                                   The normal fill color for a vertex; this also colors the target vertex in the graph if the edge is a loop.
            ----vertex_color                                                                        The color of the vertex border if the edge is a loop.
                                                                                            The defaults are listed in the notes.

        coloring_sensitivity : int (optional, default: 2)                                   Specifies how sensitive the coloring of the queue is to the number of arrivals. See the notes for how this parameter affects coloring.
        seed : int (optional)

If supplied seed is used to initialize numpy’s psuedo-random number generator.

"""


import queueing_tool as qt
import numpy as np

"""
The following code constructs an Mt/GI/5 QueueServer with mean utilization rate ρ=0.8.
The arrivals are modeled as a Poisson random measure with rate function r(t)=2+16sin2(πt/8) 
and a service distribution that is gamma with shape and scale parameters 4 and 0.1 respectively. 
To create such a queue run:
"""

def rate(t): 
    return 2 + 16 * np.sin(np.pi * t / 8)**2
def arr(t): 
    return qt.poisson_random_measure(t, rate, 18)
def ser(t): 
    return t + np.random.gamma(4, 0.1)


q = qt.QueueServer(5, arrival_f=arr, service_f=ser)
# q.set_num_servers(10)                                   # set servers in the queue
q.set_active()
q.collect_data = True
q.simulate(n=100)
data = q.fetch_data()
print(data)

"""
A comma seperated string of the column headers. Returns 'arrival,service,departure,num_queued,num_total,q_id'
1st: The arrival time of an agent.
2nd: The service start time of an agent.
3rd: The departure time of an agent.
4th: The length of the queue upon the agents arrival.
5th: The total number of Agents in the QueueServer.
6th: The QueueServer's edge index.
"""

print("the number of agents waiting in line to be served: ")
print(q.number_queued())                ## Returns the number of agents waiting in line to be served.

print("the next event is an arrival, a departure, or nothing.: ")
print(q.next_event_description())