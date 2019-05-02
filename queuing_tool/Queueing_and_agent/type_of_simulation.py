import queueing_tool as qt
import numpy as np



def event_simulation():

    rate = lambda t: 2 + 16 * np.sin(np.pi * t / 8)**2
    arr = lambda t: qt.poisson_random_measure(t, rate, 18)
    ser = lambda t: t + np.random.gamma(4, 0.1)
    q = qt.QueueServer(5, arrival_f=arr, service_f=ser, seed=54)
    q.set_active()

    q.collect_data = True
    q.simulate(100)
    data = q.fetch_data()
    print(data)

    num_events = q.num_arrivals[0] + q.num_departures
    print("the number of job arrival: ", q.num_arrivals[0])
    print("the number of job departure: ",q.num_departures)
    print("the total number of jobs ",num_events)


def time_simulation():


    rate = lambda t: 2 + 16 * np.sin(np.pi * t / 8)**2
    arr = lambda t: qt.poisson_random_measure(t, rate, 18)
    ser = lambda t: t + np.random.gamma(4, 0.1)
    q = qt.QueueServer(5, arrival_f=arr, service_f=ser, seed=54)
    q.set_active()

    num_events = q.num_arrivals[0] + q.num_departures
    t0 = q.time
    q.simulate(t=175)
    round(float(q.time - t0), 1)
    result = q.num_arrivals[1] + q.num_departures - num_events
    print(result)


def observed_new_departure():

    rate = lambda t: 2 + 16 * np.sin(np.pi * t / 8)**2
    arr = lambda t: qt.poisson_random_measure(t, rate, 18)
    ser = lambda t: t + np.random.gamma(4, 0.1)
    q = qt.QueueServer(5, arrival_f=arr, service_f=ser, seed=54)
    q.set_active()

    nA0, nD0 = q.num_arrivals[1], q.num_departures
    q.simulate(nD=1000)                                     # when 1000 departure， stop simulation
    result = q.num_departures - nD0, q.num_arrivals[1] - nA0
    print(result)



def observed_new_arrival():

    rate = lambda t: 2 + 16 * np.sin(np.pi * t / 8)**2
    arr = lambda t: qt.poisson_random_measure(t, rate, 18)
    ser = lambda t: t + np.random.gamma(4, 0.1)
    q = qt.QueueServer(5, arrival_f=arr, service_f=ser, seed=54)
    q.set_active()

    nA0, nD0 = q.num_arrivals[1], q.num_departures
    q.simulate(nA=1000)
    result =  q.num_departures - nD0, q.num_arrivals[1] - nA0,
    print(result)


if __name__ == "__main__":


    # event_simulation()
    # time_simulation()
    observed_new_departure()
    observed_new_arrival()