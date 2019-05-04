import queueing_tool as qt
import networkx as nx
import matplotlib.pyplot as plt



def draw1():

    adjacency = {
        0: {1: {'edge_type': 2}},
        1: {2: {'edge_type': 1},
            3: {'edge_type': 4}},
        2: {0: {'edge_type': 2}},
        3: {3: {'edge_type': 0}}
    }

    G = qt.QueueNetworkDiGraph(adjacency)
    print(G.lines_scatter_args(line_kwargs=None, scatter_kwargs=None, pos=None))        # not importance
    nx.draw_networkx(G)
    plt.axis('off')
    plt.show()


def draw2():

    adj1 = {
        0: {1: {}},
        1: {2: {},
            3: {}},
        3: {0: {}}}
    eTy = {0: {1: 1}, 1: {2: 2, 3: 4}, 3: {0: 1}}
    # A loop will be added to vertex 2
    g = qt.adjacency2graph(adj1, edge_type=eTy)
    ans = qt.graph2dict(g)
    print(ans)

    nx.draw_networkx(g)
    plt.axis('off')
    plt.show()


def draw3():

    adj = {0 : [1], 1: [2, 3], 3: [0]}
    eTy = {0: {1: 1}, 1: {2: 2, 3: 4}, 3: {0: 1}}
    g = qt.adjacency2graph(adj, edge_type=eTy)
    ans = qt.graph2dict(g)
    print(ans)                
    nx.draw_networkx(g)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":

    draw1()
    draw2()
    draw3()
    

