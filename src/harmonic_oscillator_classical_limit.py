from tools import Potential, Action, Metropolis, getRootDirectory
import os
import numpy as np
from multiprocessing import Pool
from pathlib import Path
import csv

# number of lattice positions
N = 100000

# parameters
mass = 0.01
mu = 10
lambda_ = 0

start, stop, step = -10, 10, 0.1

tau = 0.1

hbar_start, hbar_stop, hbar_step = 0.0, 2.0, 0.005

root_path = getRootDirectory()
dir_ = root_path / 'data' / 'harmonic_oscillator_classical_limit'
dir_.mkdir(exist_ok=True)
file_ = dir_ / ('h%0.2f-%0.2f-%0.4f_%0.2f-%0.2f-%0.2f-N%d.csv' % (hbar_start, hbar_stop, hbar_step, start, stop, step, N))
if file_.exists():
	i = input('Overwrite file "%s"? ' %file_.relative_to(root_path)).lower()
	if i == 'y':
		pass
	else:
		num = 1
		while file_.exists():
			file_ = dir_ / ('h%0.2f-%0.2f-%0.4f_%0.2f-%0.2f-%0.2f-N%d_%d.csv' % (hbar_start, hbar_stop, hbar_step, start, stop, step, N, num))
			num += 1

hbars = np.arange(hbar_start + hbar_step, hbar_stop + hbar_step, hbar_step)
bins = np.arange(start, stop + step, step=step)

def calculatePositionDistribution(hbar):
    print("calculating for hbar=%0.4f" % hbar)
    p = Potential(mu, lambda_)
    a = Action(tau, mass, p)
    m = Metropolis(N, a, borders = [-10, 10], hbar=hbar, tau=tau, initval=0)

    vals = list(m)
    return list(np.histogram(vals, bins)[0])

p = Pool()
results = p.map(calculatePositionDistribution, hbars)

with file_.open('w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['hbar'] + list(bins[:-1]))
    writer.writerow(['hbar'] + list(bins[1:]))
    for i, hbar in enumerate(hbars):
        writer.writerow([hbar] + results[i])