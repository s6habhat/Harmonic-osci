import numpy as np
from pathlib import Path
import os


def getRootDirectory():
	return Path(os.path.dirname(os.path.realpath(__file__))).parent

def getMinima(lambda_):
	# mimina at +/- sqrt(-a/(2b))
	return np.sqrt(-1 / (2 * lambda_))

def distanceToParameter(distance):
	# calculate lambda parameter from distance
	return -1/2 * (distance / 2)**-2

def bootstrap(num, values, func=np.mean):
	# bootstrap function
	return [func(np.random.choice(values, size = len(values))) for n in range(num)]

def meanSquare(values):
	return np.mean(values * values)

STATE_INIT, STATE_LEFT, STATE_RIGHT = None, 1, 2

class TransitionCounter:
	def __init__(self):
		self.transitions = -1
		self.lastState = STATE_INIT

	def registerValue(self, value):
		state = STATE_LEFT
		if value > 0:
			state = STATE_RIGHT
		if state != self.lastState:
			self.lastState = state
			self.transitions += 1

	def getTransitions(self):
		return self.transitions

def Potential(mu, lambda_):
	# Potential Energy with parameters
	def wrapper(x, mu=mu, lambda_=lambda_):
		return mu * (x ** 2 + lambda_ * x ** 4)
	return wrapper

def Kinetic(m, tau):
	# Kinetic Energy with parameters
	def wrapper(x_i, x_j, m=m, tau=tau):
		return m / 2 * (x_i - x_j) ** 2 / tau ** 2
	return wrapper

def Energy(kinetic, potential):
	# Energy function with parameters
	def wrapper(x, kinetic=kinetic, potential=potential):
		return sum([kinetic(x[i], x[i+1]) for i in range(len(x)-1)]) + sum([potential(xx) for xx in x])
	return wrapper

def deltaEnergy(kinetic, potential):
	def wrapper(x, x_old, x_new, index, kinetic=kinetic, potential=potential):
		return potential(x_new) - potential(x_old) + kinetic(x[index - 1], x_new) + kinetic(x_new, x[index + 1]) - (kinetic(x[index - 1], x_old) + kinetic(x_old, x[index + 1]))
	return wrapper

class Metropolis:
	# Metropolis algorithm
	def __init__(self, energy, deltaEnergy, init=None, initValWidth=1, valWidth=1, periodic=True, N=100, hbar=1, tau=0.1):
		if init == None:
			self.values = np.random.normal(size=N, scale=initValWidth)
		elif type(init) in [float, int]:
			self.values = np.full(N, float(init))
		else:
			self.values = np.array(init)
			N = len(self.values)
		if periodic:
			self.values[-1] = self.values[0]

		self.energy = energy
		self.deltaEnergy = deltaEnergy
		self.valWidth = valWidth
		self.periodic = periodic
		self.N = N
		self.hbar = hbar
		self.tau = tau

	def __next__(self):
		energy = self.energy(self.values)
		start = 1
		stop = self.N - 1
		accepted = 0
		for i in range(start, stop):
			newvalue = np.random.normal(self.valWidth)
			deltaEnergy = self.deltaEnergy(self.values, self.values[i], newvalue, i)
			if deltaEnergy < 0:
				self.values[i] = newvalue
				energy = energy + deltaEnergy
				accepted += 1
				# accept it

			else:
				if np.exp(- self.tau * deltaEnergy / self.hbar) > np.random.rand():
					self.values[i] = newvalue
					energy = energy + deltaEnergy
					accepted += 1
					# accept it

				# reject
		return self.values, accepted / (stop / start)

	def __iter__(self):
		return self

if __name__ == '__main__':
	# Test Case TransitionCounter
	tC = TransitionCounter()
	values = np.random.uniform(-1, 1, 10)
	for v in values:
		tC.registerValue(v)
	print(tC.getTransitions(), values)

	# Test Case getMinima, distanceToParameter
	for d in range(1, 17):
		print(distanceToParameter(d), 2 * getMinima(distanceToParameter(d)))

	# Test Case bootstrap:
	#values = np.random.normal(loc=0, scale=1, size=100)
	#bootstrap_values = bootstrap(10000, values)
	#print(bootstrap_values)