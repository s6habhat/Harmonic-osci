from tools import Potential, Action, Metropolis
from time import time

# number of lattice positions
N = 1000

# parameters
mass = 0.01
mu = 10
lambda_ = 0

tau = 0.1
hbar = 1

p = Potential(mu, lambda_)
a = Action(tau, mass, p)
m = Metropolis(N, a, borders = [-10, 10], hbar=hbar, tau=tau)


N = 100
t1 = time()
for i in range(N):
    list(m)
t2 = time()
print((t2 - t1) / N)