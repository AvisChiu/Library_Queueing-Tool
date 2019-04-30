import queueing_tool as qt
import numpy as np
import matplotlib.pyplot as plt


"""
take the arrival process to be time varying and random (more specifically, we’ll let it be a non-homogeneous Poisson process), 
with a rate that’s sinusoidal. To set that, run:
"""


def rate(t):
    
    print("Rate:",25 + 350 * np.sin(np.pi * t / 2)**2)
    return 25 + 350 * np.sin(np.pi * t / 2)**2


def arrival_rate(t):
    
    print("Possion",qt.poisson_random_measure(t, rate, 100))                             # Poission Distribution
    return qt.poisson_random_measure(t, rate, 100)


def service_rate(t):                                                           # Exponential Distribution
    
    print("Exponential",t + np.random.exponential(0.2 / 2.1))
    return t + np.random.exponential(0.2 / 2.1)



if __name__ == "__main__":
    

    ############################################
    # Create a network work graph
    # Also, the adjacency matrix can be use too.
    # The edge represtent the server type.
    ############################################

    adja_list = {0: [1], 1: [k for k in range(2, 22)]}
    edge_list = {0: {1: 1}, 1: {k: 2 for k in range(2, 22)}}
    g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)

    """
    This says there are two main types of queues/edges, type 1 and type 2. 
    All the checkout lines are of type 2 while the store queue (the edge connecting vertex zero to vertex one) is type 1. 
    The queue that represents agents leaving the store are type 0 queues, 
    and is handled automatically by queueing-tool. Now we can make our graph:
    """



    q_classes = {1: qt.QueueServer, 2: qt.QueueServer}

    q_args    = {
        1: {
            'arrival_f': arrival_rate,
            'service_f': lambda t: t,
            'AgentFactory': qt.GreedyAgent
        },
        2: {
            'num_servers': 1,
            'service_f': service_rate
        }
    }
    qn = qt.QueueNetwork(g=g, q_classes=q_classes, q_args=q_args, seed=13)


    qn.g.new_vertex_property('pos')
    pos = {}

    for v in qn.g.nodes():
        if v == 0:
            pos[v] = [0, 0.8]
        elif v == 1:
            pos[v] = [0, 0.4]
        else:
            pos[v] = [-5. + (v - 2.0) / 2, 0]

    qn.g.set_pos(pos)
    # qn.draw(fname="store.png", figsize=(12, 3), bbox_inches='tight')
    # plt.show()




    """
    ############################
    set the server:
    ############################
    """

    qn.initialize(edge_type=1)
  

    qn.clear_data()
    qn.start_collecting_data(edge_type=0)
    qn.simulate(t=3)
    data = qn.get_queue_data(edge_type=0)
    data.shape
   

    qn.draw(fname="sim.png", figsize=(12, 3), bbox_inches='tight')
    plt.show()


    

    