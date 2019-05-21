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
    


    q_classes = {1: qt.QueueServer, 2: qt.QueueServer, 3: qt.QueueServer}

    q_args    = {

        1: {
            'colors'     : {'vertex_pen' : [1,1,1,1]},
            'arrival_f': arrival_rate,
            'service_f': lambda t: t,
            'AgentFactory': qt.GreedyAgent
        },
        2: {
            'colors'     : {'vertex_pen' : [1,1,1,1]},
            'num_servers': 1,
            'service_f': service_rate
        },
        3: {
            'num_servers': 1,
            'service_f': service_rate
        }
    }


    # adja_list = {0: [1,2,4], 1: [0,3], 2:[0,5,6], 3:[1,4,8],
    #                 4:[0,3,6,9], 5:[2,7], 6:[2,4,7,10], 7:[5,6,11],
    #                 8:[3,9,12], 9:[4,8,10,13,14], 10:[6,9,11,14], 11:[7,10,15],
    #                 12:[8,13], 13:[9,12,14], 14:[9,10,13,15], 15:[11,14] }


    # edge_list = {0: {1:1,2:1,4:1}, 1: {0:1,3:1}, 2: {0:1,5:1,6:1}, 3:{1:1,4:1,8:1},
    #                 4:{0:1,3:1,6:1,9:1}, 5:{2:1,7:1}, 6:{2:1,4:1,7:1,10:1}, 7:{5:1,6:1,11:1},
    #                 8:{3:1,9:1,12:1}, 9:{4:1,8:1,10:1,13:1,14:1}, 10:{6:1,9:1,11:1,14:1},
    #                 11:{7:1,10:1,15:1}, 12:{8:1,13:1}, 13:{9:1,12:1,14:1}, 14:{9:1,10:1,13:1,15:1},
    #                 15:{11:1,14:1}}

    # adja_list = {0: [1], 1: [2,3,4], 2:[5,6] }
    # edge_list = {0: {1:1}, 1: {2:2,3:2,4:2}, 2: {5:3,6:3}}

    # adja_list = {0: [1,2,3], 1: [2, 4], 2:[1,3,4],3:[2, 4] }
    # edge_list = {0: {1:1, 2:1, 3:1}, 1: {2:2 ,4:3}, 2: {1:2,3:2,4:3}, 3: {2:2 ,4:3}}

    adja_list = {0: [1], 1: [2,3]}
    edge_list = {0: {1:1}, 1: {2:2,3:3}}

    g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)
    qn = qt.QueueNetwork(g=g, q_classes=q_classes, q_args=q_args, seed=13)
    qn.draw(fname="sim.png", figsize=(12, 3), bbox_inches='tight')

    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g,pos,node_color='green',edge_color='orange',alpha=0.6)
    nx.draw_networkx_edges(g,pos,node_color='green',edge_color='orange',alpha=0.6)
    nx.draw_networkx_labels(g,pos)

    plt.show()


    qn.initialize(edge_type=1)
    qn.clear_data()
   
    qn.start_collecting_data(edge_type=1)
    qn.start_collecting_data(edge_type=2)
    qn.start_collecting_data(edge_type=3)
    qn.simulate(100)
   
    data1 = qn.get_queue_data(edge_type=1)
    data2 = qn.get_queue_data(edge_type=2)
    data3 = qn.get_queue_data(edge_type=3)
    
    print("==========edge_type=1================")
    print(data1)
    print("==========edge_type=2================")
    print(data2)
    print("==========edge_type=3================")
    print(data3)
    
    print(len(data1),len(data2),len(data3))

    qn.animate(figsize=(12, 6)) 
 






    

   

    