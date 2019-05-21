import queueing_tool as qt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import networkx as nx
import random


def rate(t):
    
    # print("===")
    # print("time t: ", t)
    # print("Rate:",25 + 350 * np.sin(np.pi * t / 2)**2)
    
    return 25 + 350 * np.sin(np.pi * t / 2)**2

def arrival_rate(t):
    
    # print("Possion",qt.poisson_random_measure(t, rate, 100))                                  # Poission Distribution
    # print("===")
    # print(qt.poisson_random_measure(t, rate, 100))
    return qt.poisson_random_measure(t, rate, 100)

def service_rate(t):                                                                            # Exponential Distribution
    
    # print("Exponential",t + np.random.exponential(0.2 / 2.1))
    return t + np.random.exponential(0.2 / 2.1)

def transition_matrix():
    pass


def create_mat(graph,seed):

    
    mat = qt.generate_transition_matrix(graph, seed=100)
    return mat
    

def simulation(adja_list,edge_list,matrix_seed,graph_seed):

    # adja_list = {0: [1,2,3], 1: [4],2 :[4,5,6],3:[5],4:[6],5:[6],6:[7]}
    # edge_list = {0: {1:1,2:1,3:1}, 1: {4:2}, 2:{4:3,6:4,5:5}, 3:{5:6}, 4:{6:7},5:{6:8},6:{7:9}}

    s = matrix_seed
    ss = graph_seed
    
    g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)
    qn = qt.QueueNetwork(g=g, q_classes=q_classes, q_args=q_args, seed=ss, blocking='BAS')

    # mat = create_mat(g,s)
    # qn.set_transitions(mat)
    
    """
    mat = qt.generate_transition_matrix(g, seed=96)
    qn.set_transitions(mat)
    """

    qn.draw(fname="sim.png", figsize=(12, 3), bbox_inches='tight')
    # plt.show()

    qn.initialize(edge_type=1)
    qn.clear_data()
   
    qn.start_collecting_data(edge_type=1)
    qn.start_collecting_data(edge_type=2)
    qn.start_collecting_data(edge_type=3)
    qn.start_collecting_data(edge_type=4)
    qn.start_collecting_data(edge_type=5)
    qn.start_collecting_data(edge_type=6)
    qn.start_collecting_data(edge_type=7)
    qn.start_collecting_data(edge_type=8)
    qn.start_collecting_data(edge_type=9)
    qn.simulate(t=0.2)

    np.set_printoptions(suppress=True)
    data1 = qn.get_queue_data(edge_type=1)
    data2 = qn.get_queue_data(edge_type=2)
    data3 = qn.get_queue_data(edge_type=3)
    data4 = qn.get_queue_data(edge_type=4)
    data5 = qn.get_queue_data(edge_type=5)
    data6 = qn.get_queue_data(edge_type=6)
    data7 = qn.get_queue_data(edge_type=7)
    data8 = qn.get_queue_data(edge_type=8)
    data9 = qn.get_queue_data(edge_type=9)
    
    print("==========edge_type=1================")
    print(data1)
    print("==========edge_type=2================")
    # print(data2)
    # print("==========edge_type=3================")
    # print(data3)
    # print("==========edge_type=4================")
    # print(data4)
    # print("==========edge_type=5================")
    # print(data5)
    # print("==========edge_type=6================")
    # print(data6)
    # print("==========edge_type=7================")
    # print(data7)
    # print("==========edge_type=8================")
    # print(data8)
    # print("==========edge_type=9================")
    # print(data9,"\n")
    
    print("totol job of server1: ", len(data1))
    print("totol job of server2: ", len(data2))
    print("totol job of server3: ", len(data3))
    print("totol job of server4: ", len(data4))
    print("totol job of server5: ", len(data5))
    print("totol job of server6: ", len(data6))
    print("totol job of server7: ", len(data7))
    print("totol job of server8: ", len(data8))
    print("totol job of server9: ", len(data9),"\n")



    
    through_put = 0
    total_job_num = len(data1)

    counter = 0
    for i in range(len(data4)):
        if data4[i][2] != 0.:
            counter = counter +1
    through_put = through_put + counter
    print("through put of server4: ",counter)
    
    counter = 0
    for i in range(len(data7)):
        if data7[i][2] != 0.:
            counter = counter +1
    through_put = through_put + counter
    print("through put of server7: ",counter)
   
    counter = 0
    for i in range(len(data8)):
        if data8[i][2] != 0.:
            counter = counter +1
    through_put = through_put + counter
    print("through put of server8: ",counter,"\n")

    print("the through put of server4,7,8 is equal to the total number of job in server 9:", through_put)
    print("the through put of the map / the total number of jobs in map: ",through_put/total_job_num)
    # print(through_put/total_job_num)
   

    # print(qt.graph2dict(g, False))          # adjacency
    # print(qn.transitions(False)) 
    # qn.animate(figsize=(12, 6))


if __name__ == "__main__":

    
    # q_classes = {1: qt.QueueServer, 2: qt.QueueServer, 3: qt.QueueServer,4: qt.QueueServer,5: qt.QueueServer,6: qt.QueueServer,7: qt.QueueServer,8: qt.QueueServer,9: qt.QueueServer}
    q_classes = {1: qt.QueueServer, 2: qt.LossQueue, 3: qt.LossQueue,4: qt.LossQueue,5: qt.LossQueue,6: qt.LossQueue,7: qt.LossQueue,8: qt.LossQueue,9: qt.QueueServer}
    q_args    = {

        1: {
            'arrival_f': arrival_rate,
            'service_f': lambda t: t,
            # 'AgentFactory': qt.GreedyAgent                    # the agent will select the best path~!!!
                                                                # infact the agent wont be greedy.
        },
        2: {
            
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        3: {
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        4: {
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        5: {
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        6: {
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        7: {
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        8: {
            'qbuffer':0,
            'num_servers': 5,
            'service_f': service_rate
        },
        9: {
            'num_servers': 1000000,
            'service_f': service_rate
        },
    }

    adja_list = {0: [1,2,3], 1: [4],2 :[4,5,6],3:[5],4:[6],5:[6],6:[7]}
    edge_list = {0: {1:1,2:1,3:1}, 1: {4:2}, 2:{4:3,6:4,5:5}, 3:{5:6}, 4:{6:7},5:{6:8},6:{7:9}}

    for i in range(1):
        seed = random.randint(0,100)
        # print("simulation ",i,"th: ")
        simulation(adja_list,edge_list,seed,seed)

    