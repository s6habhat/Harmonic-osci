from tools import Potential, Action, Metropolis, distanceToParameter, TransitionCounter, getRootDirectory
from matplotlib import pyplot as plt
from multiprocessing import Pool
import numpy as np
import csv

# number of lattice positions
N = 10000

# number of distances evaluated
min_distance = 0.1
max_distance = 16
step_distance = 0.1

# parameters
mass = 0.01
mu = -10

tau = 0.1
hbar = 1

tunneling_rate = []

def calculateTunnelingRate(distance):
    print('Calculating transition rate for distance %0.2f' %distance)
    # calculate potential parameter
    lambda_ = distanceToParameter(distance)
    p = Potential(mu, lambda_)
    a = Action(tau, mass, p)
    m = Metropolis(N, a, borders = [-10, 10], hbar=hbar, tau=tau)

    tC = TransitionCounter()

    for value in m:
        tC.registerValue(value)
    return tC.getTransitions()

distances = np.arange(min_distance, max_distance, step_distance)
p = Pool()
tunneling_rate = p.map(calculateTunnelingRate, distances)

root_path = getRootDirectory()
dir_ = root_path / 'data' / 'tunneling_current'
dir_.mkdir(exist_ok=True)

file_ = dir_ / ('d%0.2f-%0.2f-%0.2f-N%d.csv' % (min_distance, max_distance, step_distance, N))

with file_.open('w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['distance', 'tunneling_rate'])
    for i, t_rate in enumerate(tunneling_rate):
        writer.writerow([distances[i], t_rate])
