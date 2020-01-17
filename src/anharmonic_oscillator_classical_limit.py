from tools import Potential, Action, Metropolis, getRootDirectory
import os
import numpy as np
from multiprocessing import Pool
from pathlib import Path
import csv

# number of lattice positions
N = 10000

# parameters
mass = 0.01
mu = -10
lambda_ = -0.02

start, stop, step = -10, 10, 0.1

tau = 0.1

hbar_start, hbar_stop, hbar_step = 0.01, 2.0, 0.01

hbars = np.arange(hbar_start, hbar_stop + hbar_step, hbar_step)
bins = np.arange(start, stop + step, step=step)

def calculatePositionDistribution(hbar):
	print("calculating for hbar=%0.2f" % hbar)
	p = Potential(mu, lambda_)
	a = Action(tau, mass, p)
	m = Metropolis(N, a, borders = [-10, 10], hbar=hbar, tau=tau, initval=-5)

	vals = list(m)
	return list(np.histogram(vals, bins)[0])

p = Pool()
results = p.map(calculatePositionDistribution, hbars)

root_path = getRootDirectory()
dir_ = root_path / 'data' / 'anharmonic_oscillator_classical_limit'
dir_.mkdir(exist_ok=True)

file_ = dir_ / ('h%0.2f-%0.2f-%0.2f_%0.2f-%0.2f-%0.2f-N%d.csv' % (hbar_start, hbar_stop, hbar_step, start, stop, step, N))

with file_.open('w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['hbar'] + list(bins[:-1]))
	writer.writerow(['hbar'] + list(bins[1:]))
	for i, hbar in enumerate(hbars):
		writer.writerow([hbar] + results[i])