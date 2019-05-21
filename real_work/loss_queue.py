import queueing_tool as qt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import networkx as nx

def rate(t):
    
    # print("Rate:",25 + 350 * np.sin(np.pi * t / 2)**2)
    return 25 + 350 * np.sin(np.pi * t / 2)**2

def arrival_rate(t):
    
    # print("Possion",qt.poisson_random_measure(t, rate, 100))                                  # Poission Distribution
    return qt.poisson_random_measure(t, rate, 100)

def service_rate(t):                                                                            # Exponential Distribution
    
    # print("Exponential",t + np.random.exponential(0.2 / 2.1))
    return t + np.random.exponential(0.2 / 2.1)



if __name__ == "__main__":



    q_classes = {1: qt.QueueServer, 2: qt.LossQueue, }

    q_args    = {

        1: {
            
            'arrival_f': arrival_rate,
            'service_f': lambda t: t,
            'AgentFactory': qt.GreedyAgent
        },
        2: {
            'qbuffer' : 0,
            'num_servers': 10,
            'service_f': service_rate
        },
        
    }


   

    adja_list = {0: [1], 1: [2]}
    edge_list = {0: {1:1}, 1: {2:2}}

    g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)
    qn = qt.QueueNetwork(g=g, q_classes=q_classes, q_args=q_args, seed=13)

    # qn.draw(fname="sim.png", figsize=(12, 3), bbox_inches='tight')
    # pos = nx.spring_layout(g)
    # nx.draw_networkx_nodes(g,pos,node_color='green',edge_color='orange',alpha=0.6)
    # nx.draw_networkx_edges(g,pos,node_color='green',edge_color='orange',alpha=0.6)
    # nx.draw_networkx_labels(g,pos)

    # plt.show()


    qn.initialize(edge_type=1)
    qn.clear_data()
   
    qn.start_collecting_data(edge_type=1)
    qn.start_collecting_data(edge_type=2)
    qn.start_collecting_data(edge_type=3)
    qn.simulate(t=0.2)

   

    np.set_printoptions(suppress=True)
    data1 = qn.get_queue_data(edge_type=1)
    data2 = qn.get_queue_data(edge_type=2)
    
    
    print("==========edge_type=1================")
    print(data1)
    print("==========edge_type=2================")
    print(data2)
   
    print(len(data1),len(data2))
    
    # qn.animate(figsize=(12, 6)) 

    
    m = qt.LossQueue(kwargs = q_args[2]) 
    print("\nAnother type of server : LossQueue ")
    print(m)
    print("num_blocked: ",m.num_blocked)
    print("the capacity of server: ",m.at_capacity(),"\n")
    



    

    


   
    
