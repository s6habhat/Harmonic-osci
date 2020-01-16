from tools import Potential, Action, Metropolis
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import os
import numpy as np
from multiprocessing import Pool

# number of lattice positions
N = 100000

# parameters
mass = 0.01
mu = -10
lambda_ = -0.02

start, stop = -10, 10
step = 0.1

tau = 0.1

hbar_start, hbar_stop, hbar_step = 0.01, 2.0, 0.01

hbars = np.arange(hbar_start, hbar_stop + hbar_step, hbar_step)
bins = np.arange(start, stop, step=step)
results = np.empty((len(hbars), len(bins)))

def calculatePositionDistribution(hbar):
    print("calculating for hbar=%0.2f" % hbar)
    p = Potential(mu, lambda_)
    a = Action(tau, mass, p)
    m = Metropolis(N, a, borders = [-10, 10], hbar=hbar, tau=tau, initval=-5)

    vals = list(m)
    values = np.bincount(np.digitize(vals, bins), minlength=len(bins))
    #results[i:] = values[:len(bins)]
    return values[:len(bins)]

p = Pool()
results = p.map(calculatePositionDistribution, hbars)

fig, ax = plt.subplots(figsize=(6,6))
cs = ax.imshow(results, extent=[-10, 10, max(hbars), min(hbars)], norm=LogNorm())

cbar = fig.colorbar(cs)

cbar.ax.minorticks_off()

plt.xlim(start, stop)

x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect(abs(x1-x0)/abs(y1-y0))

plt.xlabel('position')
plt.ylabel('$\\hbar$')

dir_ = 'anharmonic_oscillator_classical_limit'
script_dir = os.path.dirname(os.path.realpath(__file__))
filename = '%0.2f-%0.2f-%0.2f-%d' % (start, stop, step, N)
if not os.path.exists(script_dir + '/' + dir_):
    os.mkdir(script_dir + '/' + dir_)
plt.savefig(script_dir + '/' + dir_ + '/%s.png' %filename)
plt.savefig(script_dir + '/' + dir_ + '/%s.pdf' %filename)