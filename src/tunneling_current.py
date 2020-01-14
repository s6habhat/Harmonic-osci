from tools import Potential, Action, Metropolis, distanceToParameter, TransitionCounter
from matplotlib import pyplot as plt
from multiprocessing import Pool
import numpy as np

# number of lattice positions
N = 1000

# number of distances evaluated
n = 100
min_distance = 0.1
max_distance = 16
step_distance = 0.1

# parameters
mass = 0.01
mu = -10

tau = 0.1

tunneling_rate = []

def calculateTunnelingRate(distance):
    #print('Calculating transition rate for distance %0.2f' %distance)
    # calculate potential parameter
    lambda_ = distanceToParameter(distance)
    # start at one Minimum
    initval = distance / 2
    p = Potential(mu, lambda_)
    a = Action(tau, mass, p)
    m = Metropolis(N, a, borders = [-10, 10], initval=initval)

    tC = TransitionCounter()

    for value in m:
        tC.registerValue(value)
    return tC.getTransitions()

distances = np.arange(min_distance, max_distance, step_distance)
p = Pool()
tunneling_rate = p.map(calculateTunnelingRate, distances)

plt.plot()
plt.errorbar(distances, tunneling_rate)
plt.xlabel('Distance')
plt.ylabel('Tunneling rate')
plt.show()