from tools import Potential, Action, Metropolis
from matplotlib import pyplot as plt
import numpy as np

# number of lattice positions
N = 100000

# parameters
mass = 0.01
mu = 10
lambda_ = 0
initval = 0

step = 0.1

tau = 0.1

p = Potential(mu, lambda_)

a = Action(tau, mass, p)

m = Metropolis(N, a, borders = [-10, 10], initval=initval)

vals = list(m)

bins = np.arange(*m.borders, step=step)

values = np.bincount(np.digitize(vals, bins), minlength=len(bins))

plt.figure()
plt.errorbar(bins, values, yerr = np.sqrt(values), fmt='.')
plt.xlim(m.borders[0] / 3, m.borders[1] / 3)
plt.show()