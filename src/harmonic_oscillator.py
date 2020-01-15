from tools import Potential, Action, Metropolis
from matplotlib import pyplot as plt

# number of lattice positions
N = 1000

# parameters
mass = 0.01
mu = 10
lambda_ = 0

tau = 0.1

p = Potential(mu, lambda_)

a = Action(tau, mass, p)

m = Metropolis(N, a, borders = [-10, 10])

vals = list(m)

plt.figure()
plt.errorbar(vals, range(N))
plt.xlim(*m.borders)
plt.show()

plt.figure()
plt.hist(vals, bins = 40)
plt.xlim(m.borders[0] / 4, m.borders[1] / 4)
plt.show()