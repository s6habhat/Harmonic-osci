import random
import numpy as np
from matplotlib import pyplot as plt

N = 1000

# Harmonic oscillator
#mass = 1
#mu = 10
#lambda_ = 0
#initval = 0

# Anharmonic oscillator
mass = 0.01
mu = -10
lambda_ = -0.02
initval = -5

tau = 0.1

# mimina at +/- sqrt(-a/(2b))
print(np.sqrt(-mu/(2*mu * lambda_)))

def Potential(x):
	return mu * (x ** 2 + lambda_ * x ** 4)

def Action(x_new, x_old):
	#print(tau * (mass * (x_new - x_old) ** 2 / (2 * tau ** 2)), Potential(x_old), x_old)
	return tau * (mass * (x_new - x_old) ** 2 / (2 * tau ** 2) + Potential(x_new))

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



m = Metropolis(N, Action, borders = [-10, 10], initval=initval)

plt.plot()
plt.errorbar(list(m), range(N))
plt.xlim(*m.borders)
#xs = np.array(range(-40000, 40000)) / 1000
#plt.scatter(xs, Potential(xs))
plt.show()
