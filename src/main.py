import random
import numpy as np
from matplotlib import pyplot as plt

m = 1
lambda_ = 0

def Hamiltonian(x):
	return 0.5 * m * x ** 2 + lambda_ * x ** 4

class Metropolis:
	def __init__(self, stop, func, borders = [-5, 5], initval=0):
		self.stop = stop
		self.func = func
		self.borders = borders
		self.value = initval
		self.energy = 1000

	def __iter__(self):
		num = 0
		while num < self.stop:
			newValue = random.uniform(*self.borders)
			newEnergy = self.func(newValue)
			deltaEnergy = newEnergy - self.energy
			if deltaEnergy < 0:
				self.value = newValue
				self.energy = newEnergy
			else:
				if np.exp(-deltaEnergy) > random.random():
					self.value = newValue
					self.energy = newEnergy
			yield self.value
			num += 1

	def __len__(self):
		return self.stop

N = 1000

m = Metropolis(N, Hamiltonian)

plt.plot()
plt.scatter(list(m), range(N))
plt.xlim(*m.borders)
plt.show()