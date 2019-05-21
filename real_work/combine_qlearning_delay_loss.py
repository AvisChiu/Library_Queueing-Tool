import queueing_tool as qt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import networkx as nx
import random
import pandas as pd
import csv

"""
simulation time need to be longer as possible
"""


def check_distributtion(data):
    
    m = []
    for i in range(len(data)):
        m.append(data[i][0])
    
    for i in range(100):
        counter = 0
        for items in m :
            if items < i and items > i-1:
                counter = counter + 1
        print(counter)
     
# def rate(t): return 2 + 16 * np.sin(np.pi * t / 8)**2
# def arr(t): return qt.poisson_random_measure(t, rate, 18)
# def ser(t): return t + np.random.gamma(4, 0.1)

def rate(t):
    
    # print("===")
    # print("time t: ", t)
    # print("Rate:",25 + 350 * np.sin(np.pi * t / 2)**2)
    # return 25 + 350 * np.sin(np.pi * t / 2)**2

    m = 250 + 350 * np.sin(np.pi * t / 2)**2
    return m

   
def arrival_rate(t):
    
    # print("Possion",qt.poisson_random_measure(t, rate, 100))                                  # Poission Distribution
    # print("===")
    # print(qt.poisson_random_measure(t, rate, 100))
    # return qt.poisson_random_measure(t, rate, 100)
    # print(qt.poisson_random_measure(t, rate, 200))

    m = qt.poisson_random_measure(t, rate, 200)
    return m
   
def service_rate(t):                                                                            # Exponential Distribution
    
    # print("Exponential",t + np.random.exponential(0.2 / 2.1))

    m = t + np.random.exponential(0.2 / 2.1)
    return m

   
def transition_matrix():
    pass

def create_mat(graph,seed):

    mat = qt.generate_transition_matrix(graph, seed=100)
    return mat

def simulation(adja_list,edge_list,matrix_seed,graph_seed):

    s = matrix_seed
    ss = graph_seed
    
    g = qt.adjacency2graph(adjacency=adja_list, edge_type=edge_list)
    qn = qt.QueueNetwork(g=g, q_classes=q_classes, q_args=q_args, seed=ss, blocking='BAS')

    # mat = create_mat(g,s)
    # qn.set_transitions(mat)
    # print(qn.transitions(True))
    # mat = {0: {1: 1.0}, 1: {2: 0.0, 3: 1.0, 4: 0.0}, 
    #             2: {5: 1.0}, 3: {5: 0.0, 6: 0.0, 7: 1.0}, 4: {6: 1.0},
    #             5: {7: 1.0}, 6: {7: 1.0}, 7: {8: 1.0}, 8: {8: 1.0}}
    # qn.set_transitions(mat)
    """
    mat = qt.generate_transition_matrix(g, seed=96)
    qn.set_transitions(mat)
    """

    # qn.draw(fname="sim.png", figsize=(12, 3), bbox_inches='tight')
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
    qn.start_collecting_data(edge_type=10)
    qn.start_collecting_data(edge_type=11)
    qn.start_collecting_data(edge_type=12)
    qn.simulate(t=100)
    
    """
    len(data2), means the total job in server 2
    """
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
    data10 = qn.get_queue_data(edge_type=10)
    data11 = qn.get_queue_data(edge_type=11)
    data12 = qn.get_queue_data(edge_type=12)

    dataa1 = qn.get_agent_data(edge_type=1,return_header=False)
    dataa12 = qn.get_agent_data(edge_type=12,return_header=False)
   

    """

                ========>  重要資料作業區 <============

    """

    total_job_num = len(data1)
    job_pool = 0
    each_total_job = []                     # a list with each server's total job
    each_thoughtput = []                    # a list with each server's throughtput

    """

                ========>  重要資料作業區 <============

    """
    
    
    # print("==========edge_type=1================")
    # print(data1)
    # print("==========edge_type=2================")
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
    # print(data9)
    # print("==========edge_type=10================")
    # print(data10)
    # print("==========edge_type11================")
    # print(data11)
    # print("==========edge_type=12================")
    # print(data12)
  
  
    # print("totol job of server1: ", len(data1))
    # print("totol job of server2: ", len(data2))
    # print("totol job of server3: ", len(data3))
    # print("totol job of server4: ", len(data4))
    # print("totol job of server5: ", len(data5))
    # print("totol job of server6: ", len(data6))
    # print("totol job of server7: ", len(data7))
    # print("totol job of server8: ", len(data8))
    # print("totol job of server9: ", len(data9))
    # print("totol job of server10: ", len(data10))
    # print("totol job of server11: ", len(data11))
    # print("totol job of server12: ", len(data12),"\n")
    

    # each_total_job.append(len(data1))
    # each_total_job.append(len(data2))
    # each_total_job.append(len(data3))
    # each_total_job.append(len(data4))
    # each_total_job.append(len(data5))
    # each_total_job.append(len(data6))
    # each_total_job.append(len(data7))
    # each_total_job.append(len(data8))
    # each_total_job.append(len(data9))
    # each_total_job.append(len(data10))
    # each_total_job.append(len(data11))
    # each_total_job.append(len(data12))


    for i in range(len(data1)):
        if data1[i][2] != 0.:
            job_pool = job_pool +1
    each_thoughtput.append(job_pool)            
    # print("TOTAL NUMBER OF JOBS IN THIS SIMULATION: ",job_pool)

    # counter = 0
    # for i in range(len(data2)):
    #     if data2[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter)      
    # # print("through put of server2: ",counter)

    # counter = 0
    # for i in range(len(data3)):
    #     if data3[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server3: ",counter)

    # counter = 0
    # for i in range(len(data4)):
    #     if data4[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server4: ",counter)

    # counter = 0
    # for i in range(len(data5)):
    #     if data5[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server5: ",counter)

    # counter = 0
    # for i in range(len(data6)):
    #     if data6[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server6: ",counter)

    # counter = 0
    # for i in range(len(data7)):
    #     if data7[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server7: ",counter)

    # counter = 0
    # for i in range(len(data8)):
    #     if data8[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server8: ",counter)

    # counter = 0
    # for i in range(len(data9)):
    #     if data9[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server9: ",counter)
    
    # counter = 0
    # for i in range(len(data10)):
    #     if data10[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server9: ",counter)
   
    # counter = 0
    # for i in range(len(data11)):
    #     if data11[i][2] != 0.:
    #         counter = counter +1
    # each_thoughtput.append(counter) 
    # # print("through put of server11: ",counter)

    container = len(data12)
    each_thoughtput.append(container)
    # print("CONTAINER HAS RECIEVED: ",container,"\n")
    


    """

                ========>  重要資料作業區 <============

    """
    # server_delay = {}
    server_delay["server2"] = particular_server_delay(data2)
    server_delay["server3"] = particular_server_delay(data3)
    server_delay["server4"] = particular_server_delay(data4)
    server_delay["server5"] = particular_server_delay(data5)
    server_delay["server6"] = particular_server_delay(data6)
    server_delay["server7"] = particular_server_delay(data7)
    server_delay["server8"] = particular_server_delay(data8)
    server_delay["server9"] = particular_server_delay(data9)
    server_delay["server10"] = particular_server_delay(data10)
    server_delay["server11"] = particular_server_delay(data11)

    # server_delayy = []
    # server_delayy.append(particular_server_delay(data2))
    # server_delayy.append(particular_server_delay(data3))
    # server_delayy.append(particular_server_delay(data4))
    # server_delayy.append(particular_server_delay(data5))
    # server_delayy.append(particular_server_delay(data6))
    # server_delayy.append(particular_server_delay(data7))
    # server_delayy.append(particular_server_delay(data8))
    # server_delayy.append(particular_server_delay(data9))
    # server_delayy.append(particular_server_delay(data10))
    # server_delayy.append(particular_server_delay(data11))
    



    # debug(each_total_job,each_thoughtput)                                   # for reward
    drop = delay_and_drop_caculate(dataa1,dataa12,(job_pool-container))             # for drop rate

    # check_distributtion(data1)

    print("total job in container: ",container)
    print("compared with the container        ","the drop rate of this simulation: ", drop/container,"\n")
    print(improve_data(server_delay))
    # print(improve_data(server_delayy))


    """
                            
                ========>  重要資料作業區 <============

    """


    
    # print("the through put of the map / the total number of jobs in map: ",container/job_pool,"\n")

    # print(qn.transitions(False)) 
    # print(qt.graph2dict(g, False))          # adjacency
    # qn.animate(figsize=(12, 6))

def debug(each_total_job,each_thoughtput):

    reward = {}
    print("\n")
    print(each_total_job)
    print(each_thoughtput,"\n")

    # for i in range(len(each_total_job)):
    #     if each_total_job[i] == 0:
    #         wanna  = 1
    #         reward[i+1]=wanna
    #     else:
    #         wanna = each_thoughtput[i] / each_total_job[i]
    #         reward[i+1]=wanna

    # print(reward)

def improve_data(recv_server_delay):
    
    print(recv_server_delay)






    return 12


def particular_server_delay(particular_server):

    delay_time = []
    still_in_servicve = 0
    for i in range(len(particular_server)):
        m = particular_server[i][2]-particular_server[i][0]
        if m > 0:
            delay_time.append(m)
        else: 
            still_in_servicve = still_in_servicve + 1

    average_delay = (sum(delay_time)/len(particular_server))

    """
    caculate the sum:
    """ 

    return average_delay
    # print(still_in_servicve)
    # print(particular_server)
        

def delay_and_drop_caculate(source,destination,bias):

    biass = bias
    backup = source
    destination = [(k,destination[k]) for k in sorted(destination.keys())]          # sorted by key
    source = [(k,source[k]) for k in sorted(source.keys())]

    source_id = []
    packet_success = 0
    total_packet = len(source)
    packet_delay = {}
    drop_counter = 0
    
    for i in range(len(source)):
        source_id.append(source[i][0])
    
    for i in range(len(destination)):
        if destination[i][0] in source_id:
            # print(destination[i][0])
            packet_success = packet_success + 1 
            packet_delay[destination[i][0]] = destination[i][1][0][0] - backup[destination[i][0]][0][2]

    """
    # store_csv(packet_delay)           # store in csv
    """
    # store_csv(packet_delay)
    # print(packet_delay)

    for key in packet_delay:
        if packet_delay[key] > 0.5:
            drop_counter = drop_counter +1

    print("longer than 0.5 second : ",drop_counter)
    print("still in the system: ", biass)
    drop_counter = drop_counter + biass
    print("total drop: ",drop_counter)


    return drop_counter
       
    # print(source)                     
    # print(destination)                    # compare with id

    # print(source[0][1][0][2])
    # print(destination[0][1][0][0])
    # print(destination)

    # print(destination[i][0])              # key in dict
    # print(source[0,1][0][2])              # born time         in used
    # print(destination[0,1][0][0])         # dead time         in used
    # print(source[0][1][0][2])             # born time
    # print(destination[0][1][0][0])        # dead time


def store_csv(data):
    
    # with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    #     w = csv.DictWriter(f, data.keys())
    #     w.writeheader()
    #     w.writerow(data)
    keyList = data.keys()
    valueList = data.values()
    rows = zip(keyList, valueList)
    with open('test.csv', 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)


if __name__ == "__main__":

    server_delay = {}

    # q_classes = {1: qt.QueueServer, 2: qt.QueueServer, 3: qt.QueueServer,4: qt.QueueServer,5: qt.QueueServer,
    #              6: qt.QueueServer,7: qt.QueueServer,8: qt.QueueServer,9: qt.QueueServer, 10:qt.QueueServer, 11:qt.QueueServer, 12:qt.NullQueue}

    q_classes = {1: qt.QueueServer, 2: qt.LossQueue, 3: qt.LossQueue,4: qt.LossQueue,5: qt.LossQueue,
                 6: qt.LossQueue,7: qt.LossQueue,8: qt.LossQueue,9: qt.LossQueue, 10:qt.LossQueue, 11:qt.LossQueue, 12:qt.NullQueue}

    q_args    = {

        1: {
            'arrival_f': arrival_rate,
            'service_f': lambda t: t,
            # 'AgentFactory': qt.GreedyAgent                    # the agent will select the best path~!!!
                                                                # infact the agent wont be greedy.
        },
        2: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        3: {
            'qbuffer': 10,
            'num_servers': 12,
            'service_f': service_rate
        },
        4: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        5: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        6: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        7: {
            'qbuffer': 10,
            'num_servers': 12,
            'service_f': service_rate
        },
        8: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        9: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        10: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        11: {
            'qbuffer': 10,
            'num_servers': 6,
            'service_f': service_rate
        },
        
       
    }

    adja_list = {0: [1], 1: [2,3,4],2 :[5],3:[5,6,7],4:[6],5:[7],6:[7],7:[8]}
    edge_list = {0: {1:1}, 1: {2:2,3:3,4:4}, 2:{5:5}, 3:{5:6,7:7,6:8}, 4:{6:9}, 5:{7:10}, 6:{7:11}, 7:{8:12}}

    for i in range(1):
        seed = random.randint(0,100)
        simulation(adja_list,edge_list,seed,seed)



