from tools import Potential, Action, Metropolis, getRootDirectory, distanceToParameter
import os
import numpy as np
from multiprocessing import Pool
from pathlib import Path
import csv

# number of lattice positions
N = 100000

# parameters
mass = 0.01
mu = -10

min_distance, max_distance, step_distance = 0, 16, 0.05

start, stop, step = -10, 10, 0.1

tau = 0.1

hbar = 1

distances = np.arange(min_distance + step_distance, max_distance + step_distance, step_distance)
bins = np.arange(start, stop + step, step=step)

root_path = getRootDirectory()
dir_ = root_path / 'data' / 'anharmonic_oscillator_lambda_parameter'
dir_.mkdir(exist_ok=True)
file_ = dir_ / ('d%0.2f-%0.2f-%0.2fs%0.2f-%0.2f-%0.2f-N%d.csv' % (min_distance, max_distance, step_distance, start, stop, step, N))
if file_.exists():
	i = input('Overwrite file "%s"? ' %file_.relative_to(root_path)).lower()
	if i == 'y':
		pass
	else:
		num = 1
		while file_.exists():
			file_ = dir_ / ('d%0.2f-%0.2f-%0.2fs%0.2f-%0.2f-%0.2f-N%d_%d.csv' % (min_distance, max_distance, step_distance, start, stop, step, N, num))
			num += 1


def calculatePositionDistribution(distance):
	print("calculating for distance=%0.2f" % distance)
	lambda_ = distanceToParameter(distance)
	p = Potential(mu, lambda_)
	a = Action(tau, mass, p)
	m = Metropolis(N, a, borders = [start, stop], hbar=hbar, tau=tau, initval=-distance)

	vals = list(m)
	return list(np.histogram(vals, bins)[0])

p = Pool()
results = p.map(calculatePositionDistribution, distances)

with file_.open('w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['distance'] + list(bins[:-1]))
	writer.writerow(['distance'] + list(bins[1:]))
	for i, distance in enumerate(distances):
		writer.writerow([distance] + results[i])