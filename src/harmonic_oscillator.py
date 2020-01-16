from tools import Potential, Action, Metropolis, getRootDirectory, distanceToParameter
from matplotlib import pyplot as plt
import csv

# number of lattice positions
N = 200

# parameters
mass = 0.01
mu = 10
distance = 0
lambda_ = 0

tau = 0.1
hbar = 1

p = Potential(mu, lambda_)

a = Action(tau, mass, p)

m = Metropolis(N, a, borders = [-10, 10], hbar=hbar, tau=tau)

vals = list(m)

root_path = getRootDirectory()
dir_ = root_path / 'data' / 'harmonic_oscillator_track'
dir_.mkdir(exist_ok=True)

file_ = dir_ / ('l%0.4fd%0.4fN%d.csv' % (lambda_, distance, N))

with file_.open('w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['num', 'position'])
    for i, position in enumerate(vals):
        writer.writerow([i+1, position])