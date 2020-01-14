import random
import numpy as np
from matplotlib import pyplot as plt

def getMinima(mu, lambda_):
	# mimina at +/- sqrt(-a/(2b))
	return np.sqrt(-mu/(2*mu * lambda_))

def Potential(mu, lambda_):
	# Potential function with parameters
	def wrapper(x, mu=mu, lambda_=lambda_):
		return mu * (x ** 2 + lambda_ * x ** 4)
	return wrapper

def Action(tau, mass, potential):
	# Action function with parameters
	def wrapper(x_new, x_old, tau=tau, mass=mass, potential=potential):
		return tau * (mass * (x_new - x_old) ** 2 / (2 * tau ** 2) + potential(x_new))
	return wrapper

class Metropolis:
	# Metropolis algorithm
	def __init__(self, stop, func, borders = [-5, 5], initval=0):
		self.stop = stop
		self.func = func
		self.borders = borders
		self.value = initval
		self.energy = 1000

	def __iter__(self):
		# calculate steps
		num = 0
		while num < self.stop:
			changed = False
			while not changed:
				newValue = random.uniform(*self.borders)
				newEnergy = self.func(newValue, self.value)
				deltaEnergy = newEnergy - self.energy
				if deltaEnergy < 0:
					self.value = newValue
					self.energy = newEnergy
					changed = True
				else:
					if np.exp(-deltaEnergy) > random.random():
						self.value = newValue
						self.energy = newEnergy
						changed = True
			yield self.value
			num += 1

	def __len__(self):
		return self.stop
