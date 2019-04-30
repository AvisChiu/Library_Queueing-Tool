import queueing_tool as qt


"""
set the routing probability by yourself for any router
it wont be changed if even if the seed changed
"""
g = qt.generate_random_graph(5, seed=10)
net = qt.QueueNetwork(g)
net.transitions(False)  

net.set_transitions({1 : {2: 0.75, 3: 0.25}})
net.transitions(False)  

print(net.transitions(False))

"""
seed = 10
{0: {2: 1.0}, 1: {2: 0.75, 3: 0.25}, 2: {0: 0.3333333333333333, 1: 0.3333333333333333, 4: 0.3333333333333333}, 3: {1: 1.0}, 4: {2: 0.5, 4: 0.5}}

seed = 15
{0: {3: 1.0}, 1: {2: 0.75, 3: 0.25, 4: 0.0}, 2: {1: 0.3333333333333333, 3: 0.3333333333333333, 4: 0.3333333333333333}, 3: {0: 0.25, 1: 0.25, 2: 0.25, 4: 0.25}, 4: {1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25}}

"""