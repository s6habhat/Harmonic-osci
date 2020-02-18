from tools import Potential, Energy, deltaEnergy, Kinetic, Metropolis, getRootDirectory
import numpy as np
import csv
import argparse

parser = argparse.ArgumentParser(description='Create samples for the harmonic oscillator')
parser.add_argument("-i", "--iterations", type=int, default=100,
                    help="Number of Metropolis iterations")
parser.add_argument("-N", "--number", type=int, default=100,
                    help="Number of lattice sites")
parser.add_argument("-m", "--mass", type=float, default=0.01,
                    help="Mass of the particle")
parser.add_argument("-u", "--mu", type=float, default=10,
                    help="Depth of the potential")
parser.add_argument("-t", "--tau", type=float, default=0.1,
                    help="Time step size")
parser.add_argument("-hb", "--hbar", type=float, default=1,
                    help="Value of the reduces Plancks constant")
parser.add_argument("-init", "--initial", type=float, default=0,
                    help="Initial values for the path")
args = parser.parse_args()


# parameters
iterations = args.iterations
N = args.number
mass = args.mass
mu = args.mu
tau = args.tau
hbar = args.hbar
initial = args.initial

p = Potential(mu, 0)	# harmonic potential -> no x^4 contribution

k = Kinetic(mass, tau)

e = Energy(k, p)
de = deltaEnergy(k, p)

m = Metropolis(e, de, init=initial, valWidth=1, hbar=hbar, tau=tau, N=N)

root_path = getRootDirectory()
dir_ = root_path / 'data' / 'harmonic_oscillator_track'
dir_.mkdir(exist_ok=True)

file_ = dir_ / ('N%di%dinit%0.4f.csv' % (N, iterations, initial))

accept_ratios = []
with file_.open('w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['num'] + [str(i) for i in range(N)])
	for iteration in range(iterations):
		data, accept_ratio = next(m)
		accept_ratios.append(accept_ratio)
		writer.writerow([iteration] + list(data))
print(np.mean(accept_ratios))
