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

        1: {'arrival_f': arrival_rate,'service_f': lambda t: t,'AgentFactory': qt.GreedyAgent},
        2: {'num_servers': 1,'service_f': service_rate},
        3: {'num_servers': 1,'service_f': service_rate},
        4: {'num_servers': 1,'service_f': service_rate},
        5: {'num_servers': 1,'service_f': service_rate},
        6: {'num_servers': 1,'service_f': service_rate},
        7: {'num_servers': 1,'service_f': service_rate},
        8: {'num_servers': 1,'service_f': service_rate},
        9: {'num_servers': 1,'service_f': service_rate},
        10: {'num_servers': 1,'service_f': service_rate},
        11: {'num_servers': 1,'service_f': service_rate},
        12: {'num_servers': 1,'service_f': service_rate},
        13: {'num_servers': 1,'service_f': service_rate},
        14: {'num_servers': 1,'service_f': service_rate},
        15: {'num_servers': 1,'service_f': service_rate},

        
    }

   
    # adja_list = {0: [1,2,3], 1: [4], 2: [5,6], 3:[4,6,10], 4:[3,11], 5:[7], 6:[7,9], 7:[8], 8:[9],9:[10],10:[11] }
    # edge_list = {0: {1:1,2:1,3:1}, 1: {4:2}, 2: {5:2,6:2}, 3:{4:2,6:2,10:2} , 4:{3:2,11:2}, 5:{7:2}, 6:{7:2,9:2}, 7:{8:2}, 8:{9:2}, 9:{10:2}, 10:{11:2} }

    # adja_list = {   0: [1,2,3], 
    #                 1: [4], 
    #                 2:[5,6], 
    #                 3:[4,6,10],
    #                 4:[1,11], 
    #                 5:[2,7], 
    #                 6:[2,3,7,9], 
    #                 7:[5,6,8],
    #                 8:[7,9,15], 
    #                 9:[6,8,10,14], 
    #                 10:[3,9,11,13,14], 
    #                 11:[4,10,12],
    #                 12:[11,13], 
    #                 13:[10,12,14], 
    #                 14:[9,10,13,15], 
    #                 15:[8,14] }

    # edge_list = {   0: {1:1,2:1,3:1}, 
    #                 1: {4:2}, 
    #                 2: {5:2,6:2}, 
    #                 3:{4:2,6:2,10:2} , 
    #                 4:{1:2,11:2}, 
    #                 5:{2:2,7:2}, 
    #                 6:{2:2,3:2,7:2,9:2}, 
    #                 7:{5:2,6:2,8:2}, 
    #                 8:{7:2,9:2,15:2}, 
    #                 9:{6:2,8:2,10:2,14:2}, 
    #                 10:{3:2,9:2,11:2,13:2,14:2},
    #                 11:{4:2,10:2,12:2},
    #                 12:{11:2,13:2},
    #                 13:{10:2,12:2,14:2},
    #                 14:{9:2,10:2,13:2,15:2},
    #                 15:{8:2,14:2} }

    adja_list = {   0: [1,2,3], 
                    1: [4], 
                    2:[5,6], 
                    3:[4,6,10],
                    4:[1,11], 
                    5:[2,7], 
                    6:[2,3,7,9], 
                    7:[5,6,8],
                    8:[7,9,15], 
                    9:[6,8,10,14], 
                    10:[3,9,11,13,14], 
                    11:[4,10,12],
                    12:[11,13], 
                    13:[10,12,14], 
                    14:[9,10,13,15], 
                    15:[8,14] }

    edge_list = {   0: {1:1,2:1,3:1}, 
                    1: {4:2}, 
                    2: {5:2,6:2}, 
                    3:{4:2,6:2,10:2} , 
                    4:{1:2,11:2}, 
                    5:{2:2,7:2}, 
                    6:{2:2,3:2,7:2,9:2}, 
                    7:{5:2,6:2,8:2}, 
                    8:{7:2,9:2,15:2}, 
                    9:{6:2,8:2,10:2,14:2}, 
                    10:{3:2,9:2,11:2,13:2,14:2},
                    11:{4:2,10:2,12:2},
                    12:{11:2,13:2},
                    13:{10:2,12:2,14:2},
                    14:{9:2,10:2,13:2,15:2},
                    15:{8:2,14:2} }
                    
    
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
    qn.simulate(10)
   
    data1 = qn.get_queue_data(edge_type=1)
    data2 = qn.get_queue_data(edge_type=2)
    
    print("==========edge_type=1================")
    print(data1)
    print("==========edge_type=2================")
    print(data2)

    


    qn.animate(figsize=(12, 6))